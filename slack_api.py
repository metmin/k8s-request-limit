from slack_sdk.webhook import WebhookClient

# TODO: webhook URL configden gelicek.

def send_notification():
    url = "https://hooks.slack.com/services/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"
    webhook = WebhookClient(url)
    response = webhook.send(
        text="Deneme",
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