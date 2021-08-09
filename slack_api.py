from slack_sdk.webhook import WebhookClient

# TODO: webhook URL configden gelicek.

def send_notification(webhook_url, pod, diff):
    
    webhook = WebhookClient(webhook_url)

    response = webhook.send(
        text="Request Usage Difference Detected",
        blocks=[
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"{pod.cluster} => {pod.pod_name} => {pod.cpu_req} => {pod.cpu_usage} => {diff}"
                }
            }
        ]
    )
