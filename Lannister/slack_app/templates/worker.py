# request template that is shown to a worker
WORKER_REQUEST = [
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Bonus type:* some bonus\n*Reviewer:* some user\n" \
                "*Description: * some text\n*Status: * created"
        },
        "accessory": {
            "type": "button",
            "action_id": "edit_request",
            "text": {
                "type": "plain_text",
                "text": "Edit",
            },
            "value": "request_id"
        },
    },
]


# worker space template
WORKER = [
    {
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": "Worker Space"
        }
    },
    {
        "type": "actions",
        "elements": [
            {
                "type": "button",
                "action_id": "create_request",
                "text": {
                    "type": "plain_text",
                    "text": "Create New Request",
                },
                "style": "primary",
                "value": "create_request"
            }
        ]
    },
    {
         "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Your Requests*"
        }
    },
    {
        "type": "divider"
    },
]
