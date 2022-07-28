import requests
from os import environ

URL = environ.get("URL")


# find out which reviewer has the least requests assigned to him
def set_reviewer():

    #!

    reviewer_id = "U03MU1FH0R0"
    return reviewer_id


# create request using given data
def create_request(request):
    reviewer = set_reviewer()

    requests.post("{URL}/requests", creator=request["creator"],
     reviewer=reviewer, bonus_type=request["bonus_type"], description=
     request["description"], status="Cr")

    return reviewer


# put data into the same request using its id
def edit_request(request):
    requests.put("{URL}/requests", id=request["request_id"], bonus_type=request["bonus_type"], description=
     request["description"], status="Cr")


# set new status and change the corresponding dates to the request given
def review_request(request):
    requests.put("{URL}/requests", id=request["request_id"], status=request["status"])


# set new list of roles for a user
def edit_roles(user):  
    user_id = user["user_id"]
    requests.put("{URL}/users/{user_id}", roles=user["roles"])


# add new user
def register(user):
    info = {
        "email": user["email"],
        "username": user["login"],
        "password": user["password"],
        "slack_id": user["id"],
    }
    requests.post(f"{URL}/register", )
