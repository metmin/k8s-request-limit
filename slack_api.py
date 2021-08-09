from slack_sdk.webhook import WebhookClient

# TODO: webhook URL configden gelicek.

def send_notification(webhook_url):
    
    webhook = WebhookClient(webhook_url)

    response = webhook.send(text="Hello!")
    assert response.status_code == 200
    assert response.body == "ok"