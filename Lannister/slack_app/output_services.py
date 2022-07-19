'''
This file is just a part of app skeleton. It contains functions with dummy API information.
In fact, you should use it as a connection to real API by importing real functions and replacing these ones.
Do not forget to delete this when you are done :)
'''


# processes a query to get all requests by user_id(creator). returns requests as a list of json objects.
def get_worker_requests(user_id):
    # this is fake request list
    requests_json = [
        {
            "request_id": "requestid",
            "bonus_type": "some bonus",
            "description": "some additional information",
            "reviewer": "userid",
            "status": "created"
        },
    ]
    return requests_json


# same as get_worker_requests() but uses user_id as an id of a reviewer.
def get_reviewer_requests(user_id):
    # this is fake request list
    requests_json = [
        {
            "request_id": "requestid",
            "bonus_type": "some bonus",
            "description": "some additional information",
            "creator": "userid",
            "status": "created"
        },
    ]
    return requests_json


# a function for admin to show list of all users.
def get_users():
    # this is fake user list
    users_json = [
        {
            "user_id": "userid",
            "name": "some name",
            "email": "some@user.email",
            "roles": ['worker', 'reviewer']
        },
    ]
    return users_json


# a function for admin to show list of all requests.
def get_requests():
    # this is fake request list
    request_list = [
        {
            "request_id": "requestid",
            "bonus_type": "some bonus",
            "description": "some additional information",
            "creator": "userid",
            "reviewer": "userid",
            "status": "created"
        },
    ]
    return request_list


# a function for admin to get request history
def get_request_history(request_id):
    # this is fake request history
    request_history = {
        "date_creation": "01/06/2022",
        "date_approval": "02/06/2022",
        "date_rejection": None,
        "date_done": "03/06/2022",
    }
    return request_history


def get_user_roles(user_id):
    # this is fake response
    user_roles = ['worker', 'reviewer', 'admin']
    return user_roles
