# a request template that is shown to worker to create/edit.
WORKER_REQUEST_MODAL = [
	{
		"type": "header",
		"text": {
			"type": "plain_text",
			"text": "Enter your request information: "
		}
	},
	{
		"type": "input",
		"element": {
			"type": "plain_text_input",
			"action_id": "bonus_input_action"
		},
		"block_id": "bonus_input",
		"label": {
			"type": "plain_text",
			"text": "Bonus type",
		}
	},
	{
		"type": "input",
		"element": {
			"type": "plain_text_input",
			"action_id": "description_input_action"
		},
		"block_id": "description_input",
		"label": {
			"type": "plain_text",
			"text": "Description",
		}
	}
]


# a request template that is shown to reviewer to review.
REVIEWER_REQUEST_MODAL = [
	{
		"type": "header",
		"text": {
			"type": "plain_text",
			"text": "Request information: "
		}
	},
	{
		"type": "section",
		"text": {
			"type": "mrkdwn",
			"text": "*Creator:* creator\n*Bonus type:* bonus\n*Description:*"
		}
	},
	{
		"type": "section",
		"text": {
			"type": "plain_text",
			"text": "Some description.",
		}
	},
	{
		"type": "input",
		"block_id": "status_select",
		"element": {
			"type": "static_select",
			"placeholder": {
				"type": "plain_text",
				"text": "Set status",
			},
			"initial_option": {
				"text": {
					"type": "plain_text",
					"text": "Created",
				},
				"value": "created"
			},
			"options": [
				{
					"text": {
						"type": "plain_text",
						"text": "Created",
					},
					"value": "created"
				},
				{
					"text": {
						"type": "plain_text",
						"text": "Approved",
					},
					"value": "approved"
				},
				{
					"text": {
						"type": "plain_text",
						"text": "Rejected",
					},
					"value": "rejected"
				},
				{
					"text": {
						"type": "plain_text",
						"text": "Done",
					},
					"value": "done"
				}
			],
			"action_id": "status_select_action"
		},
		"label": {
			"type": "plain_text",
			"text": "Status",
		}
	}
]


ADMIN_REQUEST_MODAL = [
	{
		"type": "section",
		"text": {
			"type": "mrkdwn",
			"text": "*Creation date:* some_date\n*Approval date:* some_date\n" \
				"*Rejection date:* some_date\n*Done date:* some_data"
		}
	}
]
