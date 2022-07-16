from output_services import *

from templates.worker import WORKER_REQUEST, WORKER
from templates.reviewer import REVIEWER_REQUEST, REVIEWER
from templates.admin import ADMIN_REQUEST, ADMIN_USER, ADMIN, EDIT_ROLES
from templates.request import WORKER_REQUEST_MODAL, REVIEWER_REQUEST_MODAL, ADMIN_REQUEST_MODAL


# a function that uses a worker request template to fill it with real data. 
# forms a list of these items.
def worker_requests(user_id):
    requests_json = get_worker_requests(user_id)
    request_list = []

    for i in requests_json:
        item = WORKER_REQUEST[0]

        item["text"]["text"] = "*Bonus type:* {}\n*Reviewer:*" \
            " {}\n*Description:* {}\n*Status:* {}".format\
            (i["bonus_type"], i["reviewer"], i["description"], i["status"])

        item["accessory"]["value"] = "{}, {}, {}, {}".format(
            i["request_id"],
            i["bonus_type"],
            i["reviewer"],
            i["description"])
        item["block_id"] = "W{}".format(i["request_id"])
        request_list.append(item)

    return request_list


# uses a worker space template to fill it with real request list.
# returns a slack template as a json.
def worker_space(user_id):
    template = WORKER
    requests = worker_requests(user_id)

    for i in requests:
        template.append(i)
        template.append({"type": "divider"})

    return template



# same as worker_requests() but for reviewer.
def reviewer_requests(user_id):
    requests_json = get_reviewer_requests(user_id)
    request_list = []

    for i in requests_json:
            item = REVIEWER_REQUEST[0]

            item["text"]["text"] = "*Bonus type:* {}\n*Creator:*" \
                " {}\n*Description:* {}\n*Status:* {}".format\
                (i["bonus_type"], i["creator"], i["description"], i["status"])

            item["accessory"]["value"] = i["request_id"]
            item["block_id"] = "R{}".format(i["request_id"])
            request_list.append(item)
    
    return request_list


# same as worker space but for reviewer.
def reviewer_space(user_id):
    template = REVIEWER
    requests = reviewer_requests(user_id)

    for i in requests:
        template.append(i)
        template.append({"type": "divider"})

    return template


# forms a list of users as json objects.
def admin_users():
    users_json = get_users()
    user_list = []

    for i in users_json:
        item = ADMIN_USER[0]

        item["text"]["text"] = "*Name:* {}\n*Email:* " \
            "{}\n*Roles: *{}".format(i["name"], i["email"], i["roles"])

        item["accessory"]["value"] = i["user_id"]
        item["block_id"] = i["user_id"]
        user_list.append(item)

    return user_list


# forms a list of requests as json objects.
def admin_requests():
    requests_json = get_requests()
    request_list = []

    for i in requests_json:
        item = ADMIN_REQUEST[0]

        item["text"]["text"] = "*Bonus type:* {}\n*Creator:* {}\n*Reviewer:*" \
            " {}\n*Description:* {}\n*Status:* {}".format\
                (i["bonus_type"], i["creator"], i["reviewer"], \
                     i["description"], i["status"])

        item["accessory"]["value"] = i["request_id"]
        item["block_id"] = "A{}".format(i["request_id"])
        request_list.append(item)

    return request_list


# same as worker space but for admin.
def admin_space():
    template = ADMIN
    users = admin_users()
    requests = admin_requests()

    for i in users:
        template.insert(-2, i)
        template.insert(-2, {"type": "divider"})

    for i in requests:
        template.append(i)
        template.append({"type": "divider"})

    return template


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


def edit_request_modal(request):
    json_view = WORKER_REQUEST_MODAL
    json_view[1]["element"]["initial_value"] = request["bonus_type"]
    json_view[2]["element"]["initial_value"] = request["description"]

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

def review_request_modal(request):
    json_view = REVIEWER_REQUEST_MODAL
    json_view[1]["text"]["text"] = "*Creator:* {}\n*Bonus type:* {}\n" \
        "*Description:*".format(request["creator"], request["bonus_type"])
    json_view[2]["text"]["text"] = request["description"]

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


def edit_roles_modal():
    json_view = EDIT_ROLES

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


def show_history_modal(request):
    json_view = ADMIN_REQUEST_MODAL
    json_view[0]["text"] = "*Creation date:* {}\n*Approval date:* {}\n" \
				"*Rejection date:* {}\n*Done date:* {}".format(
                request["date_creation"],
                request["date_approval"],
                request["date_rejection"],
                request["date_done"])

    template = {
        "type": "modal",
        "callback_id": "show_history_view",
        "title": {"type": "plain_text", "text": "Request History"},
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
