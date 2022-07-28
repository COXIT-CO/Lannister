from output_services import (get_request_history, get_requests,
                             get_reviewer_requests, get_user_roles, get_users,
                             get_worker_requests)
from templates.admin import ADMIN, ADMIN_REQUEST, ADMIN_USER, EDIT_ROLES
from templates.registration import REGISTER_MODAL, UNREGISTERED
from templates.request import (ADMIN_REQUEST_MODAL, REVIEWER_REQUEST_MODAL,
                               WORKER_REQUEST_MODAL)
from templates.reviewer import REVIEWER, REVIEWER_REQUEST
from templates.worker import WORKER, WORKER_REQUEST


# a function that uses a worker request template to fill it with real data.
# forms a list of these items.
def worker_requests(user_id):
    requests_json = get_worker_requests(user_id)
    request_list = []

    for i in requests_json:
        item = WORKER_REQUEST[0]

        item["text"]["text"] = (
            "*Bonus type:* {}\n*Reviewer:*{}\n"
            "*Description:* {}\n*Status:* {}".format(
                i["bonus_type"], i["reviewer"], i["description"], i["status"]
            )
        )

        item["accessory"]["value"] = "{}, {}, {}, {}".format(
            i["request_id"], i["bonus_type"], i["reviewer"], i["description"]
        )
        request_list.append(item)

    return request_list


# uses a worker space template to fill it with real request list.
# returns a slack template as a json.
def worker_space(user_id):
    if "worker" in get_user_roles(user_id):
        template = []
        for i in WORKER:
            template.append(i)

        requests = worker_requests(user_id)

        for i in requests:
            template.append(i)
            template.append({"type": "divider"})

        return template
    else:
        return []


# same as worker_requests() but for reviewer.
def reviewer_requests(user_id):
    requests_json = get_reviewer_requests(user_id)
    request_list = []

    for i in requests_json:
        item = REVIEWER_REQUEST[0]

        item["text"]["text"] = (
            "*Bonus type:* {}\n*Creator:*"
            " {}\n*Description:* {}\n*Status:* {}".format(
                i["bonus_type"], i["creator"], i["description"], i["status"]
            )
        )

        item["accessory"]["value"] = "{}, {}, {}, {}".format(
            i["request_id"], i["creator"], i["bonus_type"], i["description"]
        )
        request_list.append(item)
    return request_list


# same as worker space but for reviewer.
def reviewer_space(user_id):
    if "reviewer" in get_user_roles(user_id):
        template = []
        for i in REVIEWER:
            template.append(i)
        requests = reviewer_requests(user_id)

        for i in requests:
            template.append(i)
            template.append({"type": "divider"})

        return template
    else:
        return []


# forms a list of users as json objects.
def admin_users():
    users_json = get_users()
    user_list = []

    for i in users_json:
        item = ADMIN_USER[0]

        item["text"]["text"] = "*Name:* {}\n*Email:* " "{}\n*Roles: *{}".format(
            i["name"], i["email"], i["roles"]
        )

        item["accessory"]["value"] = "{}, {}, {}, {}".format(
            i["user_id"], i["name"], i["email"], i["roles"]
        )
        user_list.append(item)

    return user_list


# forms a list of requests as json objects.
def admin_requests():
    requests_json = get_requests()
    request_list = []

    for i in requests_json:
        item = ADMIN_REQUEST[0]

        item["text"]["text"] = (
            "*Bonus type:* {}\n*Creator:* {}\n*Reviewer:*"
            " {}\n*Description:* {}\n*Status:* {}".format(
                i["bonus_type"],
                i["creator"],
                i["reviewer"],
                i["description"],
                i["status"],
            )
        )

        item["accessory"]["value"] = i["request_id"]
        request_list.append(item)

    return request_list


# same as worker space but for admin.
def admin_space(user_id):
    if "admin" in get_user_roles(user_id):
        template = []
        for i in ADMIN:
            template.append(i)

        users = admin_users()
        requests = admin_requests()

        for i in users:
            template.insert(-2, i)
            template.insert(-2, {"type": "divider"})

        for i in requests:
            template.append(i)
            template.append({"type": "divider"})

        return template
    else:
        return []


# a modal with form to fill in order to create a request.
def create_request_modal():
    json_view = WORKER_REQUEST_MODAL
    template = {
        "type": "modal",
        "callback_id": "create_request_view",
        "title": {"type": "plain_text", "text": "Create Request"},
        "submit": {
            "type": "plain_text",
            "text": "Submit",
        },
        "close": {
            "type": "plain_text",
            "text": "Cancel",
        },
        "blocks": json_view,
    }

    return template


# a modal with pre-filled form to edit in order to edit a request.
def edit_request_modal(request):
    json_view = WORKER_REQUEST_MODAL

    request_parsed = request.split(", ")
    json_view[1]["element"]["initial_value"] = request_parsed[1]

    request_description = ""
    for i in range(3, len(request_parsed)):
        request_description = ", ".join([request_description, request_parsed[i]])
    json_view[2]["element"]["initial_value"] = request_description[2:]

    json_view[1]["block_id"] = f"bonus_input_{request_parsed[0]}"
    json_view[2]["block_id"] = f"description_input_{request_parsed[0]}"

    template = {
        "type": "modal",
        "callback_id": "edit_request_view",
        "title": {"type": "plain_text", "text": "Edit Request"},
        "submit": {
            "type": "plain_text",
            "text": "Submit",
        },
        "close": {
            "type": "plain_text",
            "text": "Cancel",
        },
        "blocks": json_view,
    }

    return template


# a modal with a form to review a request.
def review_request_modal(request):
    json_view = REVIEWER_REQUEST_MODAL

    request_parsed = request.split(", ")
    json_view[1]["text"][
        "text"
    ] = "*Creator:* {}\n*Bonus type:* {}\n" "*Description:*".format(
        request_parsed[1], request_parsed[2]
    )
    request_description = ""
    for i in range(3, len(request_parsed)):
        request_description = ", ".join([request_description, request_parsed[i]])
    json_view[2]["text"]["text"] = request_description[2:]

    json_view[3]["block_id"] = f"status_select_{request_parsed[0]}"

    template = {
        "type": "modal",
        "callback_id": "review_request_view",
        "title": {"type": "plain_text", "text": "Review Request"},
        "submit": {
            "type": "plain_text",
            "text": "Submit",
        },
        "close": {
            "type": "plain_text",
            "text": "Cancel",
        },
        "blocks": json_view,
    }

    return template


# a modal with a button to add/remove reviewer role.
def edit_roles_modal(user):
    json_view = EDIT_ROLES

    if "reviewer" in user:
        json_view[0]["element"]["initial_options"] = [
            {
                "text": {
                    "type": "plain_text",
                    "text": "Reviewer",
                },
                "value": "reviewer_role",
            }
        ]

    json_view[0]["block_id"] = f"edit_roles_{user.split(', ')[0]}"

    template = {
        "type": "modal",
        "callback_id": "edit_roles_view",
        "title": {"type": "plain_text", "text": "Edit roles"},
        "submit": {
            "type": "plain_text",
            "text": "Submit",
        },
        "close": {
            "type": "plain_text",
            "text": "Cancel",
        },
        "blocks": json_view,
    }

    return template


# a modal with request history.
def show_history_modal(request):
    json_view = ADMIN_REQUEST_MODAL

    request_history = get_request_history(request)

    json_view[0]["text"]["text"] = (
        "*Creation date:* {}\n*Approval date:* "
        "{}\n*Rejection date:* {}\n*Done date:* {}".format(
            request_history["date_creation"],
            request_history["date_approval"],
            request_history["date_rejection"],
            request_history["date_done"],
        )
    )

    template = {
        "type": "modal",
        "callback_id": "show_history_view",
        "title": {"type": "plain_text", "text": "Request History"},
        "close": {
            "type": "plain_text",
            "text": "Close",
        },
        "blocks": json_view,
    }

    return template


# returns a slack template of message for unregistered users as a json.
def unregistered_view():
    template = []

    for i in UNREGISTERED:
        template.append(i)

    return template


# a modal with register form.
def register_modal():
    json_view = REGISTER_MODAL

    template = {
        "type": "modal",
        "callback_id": "register_view",
        "title": {"type": "plain_text", "text": "Registration"},
        "submit": {
            "type": "plain_text",
            "text": "Sign Up",
        },
        "close": {
            "type": "plain_text",
            "text": "Cancel",
        },
        "blocks": json_view,
    }

    return template
