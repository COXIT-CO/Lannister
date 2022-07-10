import os
# Use the package we installed
from slack_bolt import App

import views


# Initializes your app with your bot token and signing secret
app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
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
        json_view += views.admin_space(user_id)

        client.views_publish(
            user_id=user_id,
            view={
                "type": "home",
                "callback_id": "home_view",
                "blocks": json_view
            }
        )
    except Exception as e:
        logger.error(f"Error publishing home tab: {e}")


@app.action("create_request")
def render_create_request_modal(client, event, logger):
    pass


@app.action("edit_request")
def render_edit_request_modal(client, event, logger):
    pass


@app.action("review_request")
def render_review_request_modal(client, event, logger):
    pass


@app.action("edit_roles")
def render_edit_roles_modal(client, event, logger):
    pass


@app.action("show_history")
def render_show_history_modal(client, event, logger):
    pass


# Start your app
if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))
