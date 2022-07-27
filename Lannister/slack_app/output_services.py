'''
This file is just a part of app skeleton. It contains functions with dummy API information.
In fact, you should use it as a connection to real API
by importing real functions and replacing these ones.
Do not forget to delete this when you are done :)
'''


# processes a request to get all requests by user_id(creator).
# returns requests as a list of json objects.
def get_worker_requests(user_id):
    # this is fake request list
    requests_json = [
        {
            "request_id": "requestid",
            "bonus_type": "some bonus",
            "description": "some additional information",
            "reviewer": "U03MU1FH0R0",
            "status": "created"
        },
    ]
    return requests_json


# processes a request to get all requests by user_id(reviewer).
# returns requests as a list of json objects.
def get_reviewer_requests(user_id):
    # this is fake request list
    requests_json = [
        {
            "request_id": "requestid",
            "bonus_type": "some bonus",
            "description": "some additional information",
            "creator": "U03MU1FH0R0",
            "status": "created"
        },
    ]
    return requests_json


# a function for admin to show list of all users.
def get_users():
    # this is fake user list
    users_json = [
        {
            "user_id": "U03MU1FH0R0",
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
            "creator": "U03MU1FH0R0",
            "reviewer": "U03MU1FH0R0",
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


# a function to get user roles in order to render corresponding space
def get_user_roles(user_id):
    # this is fake response
    user_roles = ['worker', 'reviewer', 'admin']
    return user_roles


# a function to get creator id to notify him about his request review.
def get_request_creator(request_id):
    # this is fake request creator
    request_creator = 'U03MU1FH0R0'
    return request_creator


# a function to check if user exists. 
# sends request to fetch user data to find out if he exists.
def check_user(user_id):
    # this is fake response
    return True
