import requests
import pod_class
import pod_list_funcs
from datetime import datetime, timedelta

def get_today_yesterday ():
    now = datetime.now()
    today = now.strftime("%Y-%m-%dT%H:%M:%S")
    yesterday = (now - timedelta(days=1)).strftime("%Y-%m-%dT%H:%M:%S")
    return today, yesterday


def get_ignored_namespaces_query():
    ignore_namespaces = [
    "consul",
    #"default",
    "external",
    "gatekeeper-system",
    "goldilocks",
    "istio-system",
    "kube-node-lease",
    "kube-public",
    "kube-system",
    "logging",
    "monitoring",
    "platform",
    "ratelimit",
    "security"
    ]

    query = 'namespace!~"'
    for namespace in ignore_namespaces:
        query += namespace + '|' 
    query += '"'
    return query


# TODO prometheus_url parametresi, bu dosyanın çağırıldığı yerden verilecek, çağıran yer conf dosyasından okuyacak. - Done

def get_data(prometheus_url, query = "", with_range = False):
    params = {'query': query}

    if with_range == True:
        today, yesterday = get_today_yesterday()
        params['start'] = today
        params['end'] = yesterday

    response = requests.get(prometheus_url + '/api/v1/query', params=params)
    results = response.json()['data']['result']
    return results


#Burada "param" parametresi yerine daha iyi bir isim seçilebilir.
def set_pod_list(metrics, pod_list, param):
    for metric in metrics:
        pod_index = pod_list_funcs.get_pod_index(pod_list, metric['metric']['pod'])
        if pod_index == -1:
            pod = pod_class.Pod(metric['metric']['pod'])
            pod_list.append(pod)
            pod_index = len(pod_list) - 1

        if param == 'set_pod_request':
            pod_list[pod_index].set_pod_requests(metric['metric']['resource'], metric['value'][1])
        elif param == 'set_pod_limit':
            pod_list[pod_index].set_pod_limits(metric['metric']['resource'], metric['value'][1])
        elif param == 'cpu_usage':
            pod_list[pod_index].cpu_usage = metric['value'][1]
        elif param == 'mem_usage':
            pod_list[pod_index].mem_usage = metric['value'][1]
    return True


# Bu ve altındaki fonksiyonları birleştirebiliriz. - Nearly Done
def get_requests_from_prometheus(pod_list, prometheus_url, ignored_namespaces_query):
    query = 'kube_pod_container_resource_requests{'+ ignored_namespaces_query +'}'
    metrics = get_data(prometheus_url, query)
    _ = set_pod_list(metrics, pod_list, "set_pod_request")


def get_limits_from_prometheus(pod_list, prometheus_url, ignored_namespaces_query):
    query = 'kube_pod_container_resource_limits{'+ ignored_namespaces_query +'}'
    metrics = get_data(prometheus_url, query)
    _ = set_pod_list(metrics, pod_list, "set_pod_limit")


def get_cpu_usage_from_prometheus(pod_list, prometheus_url, ignored_namespaces_query):
    query = 'sum(irate(container_cpu_usage_seconds_total{container!="",'+ ignored_namespaces_query +'}[5m]))by(pod)'
    metrics = get_data(prometheus_url, query, True)
    _ = set_pod_list(metrics, pod_list, "cpu_usage")


def get_memory_usage_from_prometheus(pod_list, prometheus_url, ignored_namespaces_query):
    query = 'avg(container_memory_working_set_bytes{pod!="",image="",'+ ignored_namespaces_query +'})by(pod)'
    metrics = get_data(prometheus_url, query, True)
    _ = set_pod_list(metrics, pod_list, "mem_usage")
        
