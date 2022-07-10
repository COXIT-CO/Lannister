# a template of user list that is shown to admin
ADMIN_USER = [
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Name: * some name\n*Email: * some email" \
                "\n*Roles: * Worker, Reviewer"
        },
        "accessory": {
            "type": "button",
            "action_id": "edit_roles",
            "text": {
                "type": "plain_text",
                "text": "Edit roles",
                "emoji": True
            },
            "value": "user_id"
        }
    } 
]


# a list of all requests. visible to admin.
ADMIN_REQUEST = [
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Bonus type:* some bonus\n*Creator:* some user" \
                "\n*Reviewer: * some user*Description: *" \
                    "some text\n*Status: * created"
        },
        "accessory": {
            "type": "button",
            "action_id": "show_history",
            "text": {
                "type": "plain_text",
                "text": "History",
                "emoji": True
            },
            "value": "request_id"
        }
    },
]

# admin space template.
ADMIN = [
    {
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": "Admin Space",
            "emoji": True
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Users*"
        }
    },
    {
        "type": "divider"
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Requests*"
        }
    },
    {
        "type": "divider"
    },       
]
