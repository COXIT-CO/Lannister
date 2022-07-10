from .services import *

from templates.worker import WORKER_REQUEST, WORKER
from templates.reviewer import REVIEWER_REQUEST, REVIEWER
from templates.admin import ADMIN_REQUEST, ADMIN_USER, ADMIN


# a function that uses a worker request template to fill it with real data. 
# forms a list of these items.
def worker_requests(user_id):
    requests_json = get_worker_requests(user_id)
    request_list = []

    for i in requests_json:
        item = WORKER_REQUEST

        item["text"]["text"] = "*Bonus type: *{}\n*Reviewer: *" \
            "{}\n*Description: *{}\n*Status: *{}".format\
            (i["bonus_type"], i["reviewer"], i["description"], i["status"])

        item["accessory"]["value"] = i["request_id"]
        request_list.append(item)

    return request_list


# a function that uses a worker space template to fill it with real data. 
# returns a slack template as a json.
def worker_space(user_id):
    template = WORKER
    requests = worker_requests(user_id)

    for i in requests:
        template += i
        template += {"type": "divider"}

    return template



# same as worker_requests() but for reviewer.
def reviewer_requests(user_id):
    requests_json = get_reviewer_requests(user_id)
    request_list = []

    for i in requests_json:
            item = REVIEWER_REQUEST

            item["text"]["text"] = "*Bonus type: *{}\n*Creator: *" \
                "{}\n*Description: *{}\n*Status: *{}".format\
                (i["bonus_type"], i["creator"], i["description"], i["status"])

            item["accessory"]["value"] = i["request_id"]
            request_list.append(item)
    
    return request_list


# same as worker space but for reviewer.
def reviewer_space(user_id):
    template = REVIEWER
    requests = reviewer_requests(user_id)

    for i in requests:
        template += i
        template += {"type": "divider"}

    return template


# forms a list of users as json objects.
def admin_users():
    users_json = get_users()
    user_list = []

    for i in users_json:
        item = ADMIN_USER

        item["text"]["text"] = "*Name: *{}\n*Email: *" \
            "{}\n*Roles: *{}".format(i["name"], i["email"], i["roles"])

        item["accessory"]["value"] = i["user_id"]
        user_list.append(item)

    return user_list


# forms a list of requests as json objects.
def admin_requests():
    requests_json = get_requests()
    request_list = []

    for i in requests_json:
        item = ADMIN_REQUEST

        item["text"]["text"] = "*Bonus type: *{}\n*Creator: *{}\n*Reviewer: " \
            "*{}\n*Description: *{}\n*Status: *{}".format\
                (i["bonus_type"], i["creator"], i["reviewer"], i["description"], i["status"])

        item["accessory"]["value"] = i["request_id"]
        request_list.append(item)

    return request_list


# same as worker space but for admin.
def admin_space():
    template = ADMIN
    users = get_users()
    requests = get_requests()

    for i in users:
        template.insert(-2, i)
        template.insert(-2, {"type": "divider"})

    for i in requests:
        template.append(i)
        template.append({"type": "divider"})

    return template
