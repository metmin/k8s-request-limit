from slack_sdk.webhook import WebhookClient

# TODO: webhook URL configden gelicek.

def send_notification(webhook_url, diff_message, error_message):
    
    """
    # Burası ayrı bir fonksiyondan gelebilir.
    if notification_type == "DIFF":
        title = "Request Usage Difference Detected"
        message = f"Cluster Name: {pod.cluster}\nPod Name: {pod.pod_name}\nCPU Request: {pod.cpu_req}\nCPU Usage: {pod.cpu_usage}\nCPU Diff: %{cpu_diff}\nMem Request: {pod.cpu_req}\nMem Usage: {pod.cpu_usage}\nMem Diff: %{mem_diff}"
    elif notification_type == "ERROR":
        title = "Error Detected"
        message = f"There is an error about {pod.cluster}/{pod.pod_name} cpu or memory request"
    else:
        return 0
    """

    webhook = WebhookClient(webhook_url)

    response = webhook.send(
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

    response = webhook.send(
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

    return response