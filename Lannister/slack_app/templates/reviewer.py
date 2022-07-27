# request template that is shown to a reviewer.
REVIEWER_REQUEST = [
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Bonus type:* some bonus\n*Creator:* some user" \
                "\n*Description: * some text\n*Status: * created"
        },
        "accessory": {
            "type": "button",
            "action_id": "review_request",
            "text": {
                "type": "plain_text",
                "text": "Review",
            },
            "value": "request_id"
        }
    },
]


# reviewer space template
REVIEWER = [
    {
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": "Reviewer Space",
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Requests assigned to You*"
        }
    },
    {
        "type": "divider"
    },
]
