import os
# Use the package we installed
from slack_bolt import App

import views
from input_services import *


# Initializes your app with your bot token and signing secret
app = App(
    token=os.getenv("SLACK_BOT_TOKEN"),
    signing_secret=os.getenv("SLACK_SIGNING_SECRET")
)


# an internal function to update home tab after a change of data
def new_home_tab(user, logger):
    try:
        json_view = views.worker_space(user)
        json_view += views.reviewer_space(user)
        json_view += views.admin_space(user)

        return json_view
    except Exception as e:
        logger.error(f"Error updating home tab: {e}")



# Home tab
@app.event("app_home_opened")
def publish_home_tab(client, event, logger):
    try:
        user_id = event["user"]

        json_view = views.worker_space(user_id)
        json_view += views.reviewer_space(user_id)
        json_view += views.admin_space(user_id)

        client.views_publish(
            user_id=user_id,
            view={
                "type": "home",
                "callback_id": "home_view",
                "blocks": str(json_view)
            }
        )
    except Exception as e:
        logger.error(f"Error publishing home tab: {e}")


@app.action("create_request")
def render_create_request_modal(ack, body, client, logger):
    try:
        ack()
        client.views_open(
            trigger_id=body["trigger_id"],
            view = views.create_request_modal()
        )
    except Exception as e:
        logger.error(f"Error while opening modal: {e}")


@app.action("edit_request")
def render_edit_request_modal(ack, body, client, logger):
    try:
        ack()
        client.views_open(
            trigger_id=body["trigger_id"],
            view = views.edit_request_modal(body["actions"][0]["value"])
        )
    except Exception as e:
        logger.error(f"Error while opening modal: {e}")


@app.action("review_request")
def render_review_request_modal(ack, body, client, logger):
    try:
        ack()
        client.views_open(
            trigger_id = body["trigger_id"],
            view = views.review_request_modal(body["actions"][0]["value"])
        )
    except Exception as e:
        logger.error(f"Error while opening modal: {e}")


@app.action("edit_roles")
def render_edit_roles_modal(ack, body, client, logger):
    try:
        ack()
        client.views_open(
            trigger_id = body["trigger_id"],
            view = views.edit_roles_modal(body["actions"][0]["value"])
        )
    except Exception as e:
        logger.error(f"Error while opening modal: {e}")


@app.action("show_history")
def render_show_history_modal(ack, body, client, logger):
    try:
        ack()
        client.views_open(
            trigger_id = body["trigger_id"],
            view = views.show_history_modal(body["actions"][0]["value"])
        )
    except Exception as e:
        logger.error(f"Error while opening modal: {e}")


@app.view("create_request_view")
def create_request_submission(ack, body, client, say, logger):
    try:
        ack()
        request_info = {}

        for k,v in body["view"]["state"]["values"].items():
            request_info[k] = v
        
        create_request(request_info)
        say("A new request has been assigned to you.",
         channel='D03NXC4SCNM') #! send to reviewer
        

        client.views_update(view_id=body["view"]["id"], 
        hash=body["view"]["hash"], view={
            "type": "home",
            "callback_id": "home_view",
            "blocks": str(new_home_tab(body["user"], logger))
        })
    except Exception as e:
        logger.error(f"Error while submitting data: {e}")


@app.view("edit_request_view")
def edit_request_submission(ack, body, client, say, logger):
    try:
        ack()
        request_info = {}

        for k,v in body["view"]["state"]["values"].items():
            request_info[k] = v
        
        edit_request(request_info)

        client.views_update(view_id=body["view"]["id"], 
        hash=body["view"]["hash"], view={
            "type": "home",
            "callback_id": "home_view",
            "blocks": str(new_home_tab(body["user"], logger))
        })
    except Exception as e:
        logger.error(f"Error while submitting data: {e}")


@app.view("review_request_view")
def review_request_submission(ack, body, client, say, logger):
    try:
        ack()
        request_info = {}

        for k,v in body["view"]["state"]["values"].items():
            request_info[k] = v
        
        review_request(request_info)
        say("Your request has been reviewed.",
         channel='D03NXC4SCNM') #! send to creator
        

        client.views_update(view_id=body["view"]["id"], 
        hash=body["view"]["hash"], view={
            "type": "home",
            "callback_id": "home_view",
            "blocks": str(new_home_tab(body["user"], logger))
        })
    except Exception as e:
        logger.error(f"Error while submitting data: {e}")


@app.view("edit_roles_view")
def edit_roles_submission(ack, body, client, say, logger):
    try:
        ack()
        roles_info = {}

        roles_info["roles"] = body["view"]["state"]["values"]["edit_roles"]["set_reviewer_role"]["value"]
        
        edit_roles(roles_info)
        say("Your role has been changed.",
         channel='D03NXC4SCNM') #! send to user whose role was changed
        

        client.views_update(view_id=body["view"]["id"], 
        hash=body["view"]["hash"], view={
            "type": "home",
            "callback_id": "home_view",
            "blocks": str(new_home_tab(body["user"], logger))
        })
    except Exception as e:
        logger.error(f"Error while submitting data: {e}")

# Start your app
if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))
