from slack_sdk.webhook import WebhookClient

# TODO: webhook URL configden gelicek.

def send_notification(webhook_url):
    
    webhook = WebhookClient(webhook_url)

    response = webhook.send(
        text="fallback",
        blocks=[
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "You have a new request:\n*<fakeLink.toEmployeeProfile.com|Fred Enriquez - New device request>*"
                }
            }
        ]
    )
