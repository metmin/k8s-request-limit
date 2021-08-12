from slack_sdk.webhook import WebhookClient

# TODO: webhook URL configden gelicek.

def send_notification(webhook_url, diff_message, error_message):
    webhook = WebhookClient(webhook_url)

    response_diff = webhook.send(
        text="Request Usage Difference Detected",
        blocks=[
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": diff_message
                }
            }
        ]
    )

    response_err = webhook.send(
        text="Error Detected",
        blocks=[
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": error_message
                }
            }
        ]
    )

    return response_diff, response_err