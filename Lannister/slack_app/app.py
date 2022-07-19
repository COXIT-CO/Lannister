import os
# Use the package we installed
from slack_bolt import App

import views
from input_services import *


HOME_ID = "to_be_filled"

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
        return None



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
        global HOME_ID
        HOME_ID = event["view"]["id"]
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
        request_info = {
            "bonus": body["view"]["state"]["values"]["bonus_input"]\
                ["bonus_input_action"]["value"],
            "description": body["view"]["state"]["values"]["description_input"]\
                ["description_input_action"]["value"],
        }
        
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
def edit_request_submission(ack, body, client, logger):
    try:
        ack()

        values_dict = body["view"]["state"]["values"]
        request_id = list(values_dict.keys())[0].split('_')[-1]

        request_info = {
            "request_id": request_id,
            "bonus": values_dict[f"bonus_input_{request_id}"]\
                ["bonus_input_action"]["value"],
            "description": values_dict[f"description_input_{request_id}"]\
                ["description_input_action"]["value"],
        }
        
        edit_request(request_info)

        global HOME_ID
        client.views_update(view_id=HOME_ID, view={
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

        values_dict = body["view"]["state"]["values"]
        request_id = list(values_dict.keys())[0].split('_')[-1]

        request_info = {
            "request_id": request_id,
            "status": values_dict[f"status_select_{request_id}"]\
                ["status_select_action"]["selected_option"]["value"],
        }
        
        review_request(request_info)
        say("Your request has been reviewed.",
         channel='D03NXC4SCNM') #! send to creator
        
        global HOME_ID
        client.views_update(view_id=HOME_ID, view={
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

        values_dict = body["view"]["state"]["values"]
        user_id = list(values_dict.keys())[0].split('_')[-1]

        roles_info = {
            "user_id": user_id,
            "roles": values_dict[f"edit_roles_{user_id}"]\
            ["set_reviewer_role"]["selected_options"][0]["value"],
        }
        
        edit_roles(roles_info)
        say("Your role has been changed.",
         channel='D03NXC4SCNM') #! send to user whose role was changed
        

        client.views_update(view_id=HOME_ID, view={
            "type": "home",
            "callback_id": "home_view",
            "blocks": str(new_home_tab(body["user"], logger))
        })
    except Exception as e:
        logger.error(f"Error while submitting data: {e}")

# Start your app
if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))
