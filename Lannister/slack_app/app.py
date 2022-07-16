import os
# Use the package we installed
from slack_bolt import App

import views


# Initializes your app with your bot token and signing secret
app = App(
    token=os.getenv("SLACK_BOT_TOKEN"),
    signing_secret=os.getenv("SLACK_SIGNING_SECRET")
)


# Home tab
@app.event("app_home_opened")
def update_home_tab(client, event, logger):
    try:
        user_id = event["user"]
        # default worker rights
        json_view = views.worker_space(user_id)

        # PSEUDO if authorized user has reviewer role:
        json_view += views.reviewer_space(user_id)

        # PSEUDO if authorized user has admin role:
        json_view += views.admin_space()

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
def render_create_request_modal(ack, body, client, logger, say):
    try:
        ack()
        say("I've got your request. 200 OK")
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
        request_info = {"bonus_type": None, "description": None} #! Need to implement logic
        client.views_open(
            trigger_id=body["trigger_id"],
            view = views.edit_request_modal(request_info)
        )
    except Exception as e:
        logger.error(f"Error while opening modal: {e}")


@app.action("review_request")
def render_review_request_modal(ack, body, client, logger):
    try:
        ack()
        request_info = {"bonus_type": None, "description": None,\
             "creator": None} #! Need to implement logic
        client.views_open(
            trigger_id = body["trigger_id"],
            view = views.review_request_modal(request_info)
        )
    except Exception as e:
        logger.error(f"Error while opening modal: {e}")


@app.action("edit_roles")
def render_edit_roles_modal(ack, body, client, logger):
    try:
        ack()
        client.views_open(
            trigger_id = body["trigger_id"],
            view = views.edit_roles_modal()
        )
    except Exception as e:
        logger.error(f"Error while opening modal: {e}")


@app.action("show_history")
def render_show_history_modal(ack, body, client, logger):
    try:
        ack()
        request_info = {"date_creation": None, "date_approval": None, \
            "date_rejection": None, "date_done": None} 
        #! Need to implement logic
        client.views_open(
            trigger_id = body["trigger_id"],
            view = views.show_history_modal(request_info)
        )
    except Exception as e:
        logger.error(f"Error while opening modal: {e}")


# Start your app
if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))
