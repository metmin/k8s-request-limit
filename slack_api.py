from slack_sdk.webhook import WebhookClient

def send_notification(webhook, title, message):
    _ = webhook.send(
        text=title,
        blocks=[
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": message
                }
            }
        ]
    )

def send_diff_notification(webhook_url, diff_list):

    webhook = WebhookClient(webhook_url)
    title = "Request Usage Difference Detected"
    diff_message = ""

    for team, pods in diff_list.items():
        for pod in pods:
            temp_message = f"```Team Name: {team}\nCluster Name: {pod['cluster']}\n\tPod Name: {pod['pod']}\n\t\tCPU Request: {pod['cpu_req']}\n\t\tCPU Usage: {pod['cpu_usage']}\n\t\tCPU Diff: %{pod['cpu_diff']}\n\t\t--------------------\n\t\tMem Request: {pod['mem_req']}\n\t\tMem Usage: {pod['mem_usage']}\n\t\tMem Diff: %{pod['mem_diff']}```\n"

            if (len(diff_message) + len(temp_message) > 3000):              
                send_notification(webhook, title, diff_message)        
                diff_message = ""

            diff_message += temp_message            

    if len(diff_message) > 0 :
        send_notification(webhook, title, diff_message)

    return True
