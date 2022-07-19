# a template of user list that is shown to admin
ADMIN_USER = [
    {
        "type": "section",
        "block_id": "user_id",
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
            },
            "value": "user_id"
        }
    } 
]


# a list of all requests. visible to admin.
ADMIN_REQUEST = [
    {
        "type": "section",
        "block_id": "admin_request_id",
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


# an admin template to add/remove reviewer role.
EDIT_ROLES = [
	{
		"type": "input",
        "optional": True,
        "block_id": "edit_roles_id",
		"element": {
			"type": "checkboxes",
			"options": [
				{
					"text": {
						"type": "plain_text",
						"text": "Reviewer",
					},
					"value": "reviewer_role"
				}
			],
			"action_id": "set_reviewer_role",
		},
		"label": {
			"type": "plain_text",
			"text": "Do you want to grant this user with reviewer rights?",
		}
	},
]
