import prometheus_api
import pod_list_funcs
import slack_api
import config
from flask import Flask, render_template

app = Flask(__name__)

headings = [
    "Team",
    "Cluster",
    "Pod",
    "Cpu Request",
    "Cpu Usage",
    "Cpu Difference [%]",
    "Memory Request [Mb]",
    "Memory Usage [Mb]",
    "Memory Difference [%]",
]

pod_list = []

@app.route("/")
def table():
    global pod_list

    if len(pod_list) == 0:

        for prometheus_url in config.PROMETHEUS:
            pod_list_temp = []
            query = prometheus_api.get_ignored_namespaces_query()

            prometheus_api.get_requests_from_prometheus(
                pod_list_temp, prometheus_url, query)

            prometheus_api.get_limits_from_prometheus(
                pod_list_temp, prometheus_url, query)

            prometheus_api.get_cpu_usage_from_prometheus(
                pod_list_temp, prometheus_url, query)
    
            prometheus_api.get_memory_usage_from_prometheus(
                pod_list_temp, prometheus_url, query)

            pod_list += pod_list_temp

    diff_list = pod_list_funcs.calculate_diff(pod_list)
    # print(diff_message)
    # _ = slack_api.send_diff_notification(config.WEBHOOK_URL, diff_list)

    return render_template("table.html", headings=headings, data=diff_list)
