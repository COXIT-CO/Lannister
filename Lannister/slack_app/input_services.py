# find out which reviewer has the least requests assigned to him
def set_reviewer():
    reviewer_id = 'U03MU1FH0R0'
    return reviewer_id

# create request using given data
def create_request(request):
    # here must be a POST request to a corresponding API endpoint
    # we will return request reviewer to notify him when
    # a new request is assigned to him
    return set_reviewer()

# put data into the same request using its id
def edit_request(request):    
    # here must be a PUT request to a corresponding API endpoint
    pass


# set new status and change the corresponding dates to the request given
def review_request(request):
    # here must be a PUT request to a corresponding API endpoint
    pass


# set new list of roles for a user
def edit_roles(user):
    # here must be a PUT request to a corresponding API endpoint
    pass
