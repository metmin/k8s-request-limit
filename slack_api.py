from slack_sdk.webhook import WebhookClient

# TODO: webhook URL configden gelicek.

def send_notification():
    url = "https://hooks.slack.com/services/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"
    
    webhook = WebhookClient(url)

    response = webhook.send(text="Hello!")
    assert response.status_code == 200
    assert response.body == "ok"