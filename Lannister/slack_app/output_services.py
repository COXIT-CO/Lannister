import requests
from os import environ


URL = environ.get("URL")


def get_by_slack_id(slack_id):
    response = requests.get(f"{URL}/users/slack/{slack_id}")
    user_id = response.data["id"]
    return user_id


# processes a request to get all requests by slack_id(creator).
# returns requests as a list of json objects.
def get_worker_requests(slack_id):

    response = requests.get(f"{URL}/requests/worker/{get_by_slack_id(slack_id)}")
    requests_json = []

    for i in response.data:
        item = {
            "request_id": i["id"],
            "bonus_type": i["bonus_type"],
            "description": i["description"],
            "reviewer": i["reviewer"],
            "status": i["status"],
        }
        requests_json.append(item)
    
    return requests_json


# processes a request to get all requests by slack_id(reviewer).
# returns requests as a list of json objects.
def get_reviewer_requests(slack_id):
    
    response = requests.get(f"{URL}/requests/reviewer/{get_by_slack_id(slack_id)}")
    requests_json = []

    for i in response.data:
        item = {
            "request_id": i["id"],
            "bonus_type": i["bonus_type"],
            "description": i["description"],
            "creator": i["creator"],
            "status": i["status"],
        }
        requests_json.append(item)
    
    return requests_json


# a function for admin to show list of all users.
def get_users():
    
    response = requests.get(f"{URL}/users")
    users_json = []

    for i in response.data:
        item = {
            "user_id": i["id"],
            "name": i["username"],
            "email": i["email"],
            "roles": i["roles"],#!
        }
        users_json.append(item)

    return users_json


# a function for admin to show list of all requests.
def get_requests():

    response = requests.get(f"{URL}/requests")
    request_list = []

    for i in response.data:
        item = {
            "request_id": i["id"],
            "bonus_type": i["bonus_type"],
            "description": i["description"],
            "creator": i["creator"],
            "reviewer": i["reviewer"],
            "status": i["status"],
        }
        request_list.append(item)

    return request_list


# a function for admin to get request history
def get_request_history(request_id):

    response = requests.get(f"{URL}/request_history/{request_id}")
    request_history = []

    for i in response.data:
        item = {
            "date_creation": i["date_created"],
            "date_approval": i["date_approved"],
            "date_rejection": i["date_rejected"],
            "date_done": i["date_done"],
        }
        request_history.append(item)

    return request_history


# a function to get user roles in order to render corresponding space
def get_user_roles(slack_id):
    
    response = requests.get(f"{URL}/users/{get_by_slack_id(slack_id)}")

    user_roles = response.data["roles"]#!
    return user_roles


# a function to get creator id to notify him about his request review.
def get_request_creator(request_id):
    
    response = requests.get(f"{URL}/requests/{request_id}")

    request_creator = response.data["slack_id"]
    return request_creator


# a function to check if user exists.
# sends request to fetch user data to find out if he exists.
def check_user(slack_id):
    
    response = requests.get(f"{URL}/users/slack/{slack_id}")

    if response.data["id"]:
        return True

    return False
