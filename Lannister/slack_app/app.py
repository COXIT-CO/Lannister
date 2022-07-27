import os
# Use the package we installed
from slack_bolt import App

import views
from input_services import create_request, edit_request, review_request, edit_roles
from output_services import get_request_creator


# Initializes your app with your bot token and signing secret
app = App(
    token=os.getenv("SLACK_BOT_TOKEN"),
    signing_secret=os.getenv("SLACK_SIGNING_SECRET")
)


# Home tab
@app.event("app_home_opened") #! problem here
def publish_home_tab(client, event, logger):
    try:
        user_id = event["user"]
        
        json_view = []
        json_view = views.worker_space(user_id)
        for i in views.reviewer_space(user_id):
            json_view.append(i)
        for i in views.admin_space(user_id):
            json_view.append(i)

        client.views_publish(
            user_id=user_id,
            view={
                "type": "home",
                "blocks": json_view,
            },
        )
    except Exception as e:
        logger.error(f"Error publishing home tab: {e}")


# a listener of a "create_request" action. triggered by Create Request button.
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


# a listener of an "edit_request" action. triggered by Edit button.
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


# a listener of a "review_request" action. triggered by Review button.
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


# a listener of an "edit_roles" action. triggered by Edit roles button.
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


# a listener of a "show_history" action. triggered by Show History button.
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


# a listener of a "create_request_view" view submission.
# triggered by Submit button of create_request_modal.
@app.view("create_request_view")
def create_request_submission(ack, body, say, logger):
    try:
        ack()

        values_dict = body["view"]["state"]["values"]
        request_id = list(values_dict.keys())[0].split('_')[-1]

        request_info = {
            "bonus": values_dict[f"bonus_input_{request_id}"]\
                ["bonus_input_action"]["value"],
            "description": values_dict[f"description_input_{request_id}"]\
                ["description_input_action"]["value"],
        }
        say("A new request has been assigned to you.",
         channel=create_request(request_info))
    except Exception as e:
        logger.error(f"Error while submitting data: {e}")


# a listener of a "edit_request_view" view submission.
# triggered by Submit button of edit_request_modal.
@app.view("edit_request_view")
def edit_request_submission(ack, body, logger):
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
    except Exception as e:
        logger.error(f"Error while submitting data: {e}")


# a listener of a "review_request_view" view submission.
# triggered by Submit button of review_request_modal.
@app.view("review_request_view")
def review_request_submission(ack, body, say, logger):
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
         channel=get_request_creator(request_id))
        
    except Exception as e:
        logger.error(f"Error while submitting data: {e}")


# a listener of a "edit_roles_view" view submission.
# triggered by Submit button of edit_roles_modal.
@app.view("edit_roles_view")
def edit_roles_submission(ack, body, say, logger):
    try:
        ack()

        values_dict = body["view"]["state"]["values"]
        user_id = list(values_dict.keys())[0].split('_')[-1]
        try:
            roles = ['worker'].append(values_dict[f"edit_roles_{user_id}"]\
            ["set_reviewer_role"]["selected_options"][0]["value"])
        except IndexError:
            roles = ['worker']

        roles_info = {
            "user_id": user_id,
            "roles": roles,
        }
        
        edit_roles(roles_info)
        say("Your role has been changed.",
         channel=user_id)
        
    except Exception as e:
        logger.error(f"Error while submitting data: {e}")


# Start your app
if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))
