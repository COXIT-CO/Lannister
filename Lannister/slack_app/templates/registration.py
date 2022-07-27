UNREGISTERED = [
    {
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": "Oops! It seems you are not registered.",
        }
    },
    {
        "type": "actions",
        "elements": [
            {
                "type": "button",
                "text": {
                    "type": "plain_text",
                    "text": "Sign Up",
                },
                "action_id": "register"
            }
        ]
    },
]

REGISTER_MODAL = [
	{
		"type": "input",
        "block_id": "login_input",
		"element": {
			"type": "plain_text_input",
			"action_id": "login_input_action"
		},
		"label": {
			"type": "plain_text",
			"text": "Login",
		}
	},
	{
		"type": "input",
        "block_id": "password_input",
		"element": {
			"type": "plain_text_input",
			"action_id": "password_input_action"
		},
		"label": {
			"type": "plain_text",
			"text": "Password",
		}
	}
]
