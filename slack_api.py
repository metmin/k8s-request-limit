from slack_sdk.webhook import WebhookClient

# TODO: webhook URL configden gelicek.

def send_diff_notification(webhook_url, pod, cpu_diff, mem_diff):
    webhook = WebhookClient(webhook_url)

    response = webhook.send(
        text="Request Usage Difference Detected",
        blocks=[
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"Cluster Name: {pod.cluster}\nPod Name: {pod.pod_name}\nCPU Request: {pod.cpu_req}\nCPU Usage: {pod.cpu_usage}\nCPU Diff: %{cpu_diff}\nMem Request: {pod.cpu_req}\nMem Usage: {pod.cpu_usage}\nMem Diff: %{mem_diff}"
                }
            }
        ]
    )

def send_error_notification(webhook_url):
    webhook = WebhookClient(webhook_url)

    response = webhook.send(
        text="Request Usage Difference Detected",
        blocks=[
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "There is an error about cpu or memory request"
                }
            }
        ]
    )