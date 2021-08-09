from slack_sdk.webhook import WebhookClient

# TODO: webhook URL configden gelicek.

def send_notification():
    url = "https://hooks.slack.com/services/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"
    
    webhook = WebhookClient(url)

    response = webhook.send(text="Hello!")
    assert response.status_code == 200
    assert response.body == "ok"