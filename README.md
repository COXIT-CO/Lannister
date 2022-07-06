# API
_______
### Fetch information about all users.

This method shows all registered users.

**GET <base_url>/users/**

Return:

    200: content found
    400: bad request
    401: unauthorized 
    403: forbidden
    500: internal server error 
    
    
_________________________________________________________________________
### Fetch information about reviewers.

This method shows all reviewers.

**GET <base_url>/reviewers/**

Return:

    200: Content found
    400: bad request
    404: file not found 
    500: internal server error 
_________________________________________________________________________

### Fetch information about requests.

This method shows all requests.

**GET <base_url>/requests/**

Return:

    200: Content found
    400: bad request
    404: file not found 
    500: internal server error 
    
__________________________________________________________________________

### Fetch information about request.

This method shows single request .

**GET <base_url>/requests/<request_id>**

Return


    200: сontent found
    400: bad request
    404: file not found 
    500: internal server error  
    
__________________________________________________________________________
### User registration

**POST <base_url>/registration**

The payload MUST contain the following json properties:

 *name*: username ,

 *email*: your work email , 

 *password*: your account password , 


Return:

    201: + the request: Created
    400: bad request


__________________________________________________________________________

### Generate a request


Worker create new request with info: bonus-type,description, and she/he choose reviewer.

**POST <base_url>/request**

The payload MUST contain the following json properties:

 *creator*: Worker who create the request ,

 *reviewer*: A person who is assigned to review the request, 

 *bonus_type*: It can be a referral bonus, overtime, etc ,

*description*: information about the bonus,


Return:

    201 + the request: Created
    404 Content not found
    401: unauthorized 
__________________________________________________________________________

### Add role

The admin can choose single user to add Reviewr role.

**POST <base_url>/user/<user_id>/<user_role>**

The payload MUST contain the following json properties:

*name*: the username

*email*:the user email

*roles*: role in the company

Return:

     201: + the user: Created
     400: bad request
     403: forbidden


__________________________________________________________________________
### Edit the selected request.

The worker can change the selected request.

**PUT <base_url>/request/<request_id>**

Payload: it is a json payload structured like:

{  <br><br>
    "creator" : "< value >",<br><br>
    "reviewer": "< value >",<br><br>
    "bonus_type": "< value >",<br><br>
    "description": "< value >",<br><br>
    "status": "< value >"<br><br>
}

Return:

    200: content found (OK: file updated and db updated )
    201: the content was added (created)
    400: bad request (File not saved) 
    401: unauthorized 
    404: not found (File not found) 
    500: internal server error (File was copied, but database was not updated)

__________________________________________________________________________
### Remove role
The admin can choose single user to remove Reviewer role.

**DELETE <base_url>/user/<user_id>/<user_role>**

Return:

    200: content found 
    204: no content 
    400: bad request
    403: forbidden
    404: not found (File not found) 

__________________________________________________________________________
### Remove request
The user can delete the selected request

**DELETE <base_url>/request/<request_id>**

Return:

    200: content found
    204: no content
    400: bad request
    403: forbidden
    404: not found (File not found) 