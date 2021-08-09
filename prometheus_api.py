import requests
import pod_class
import pod_list_funcs

def get_ignores():
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

    query = ""
    for namespace in ignore_namespaces:
        query += f'namespace!="{namespace}",' 

    return query


# TODO prometheus_url parametresi, bu dosyanın çağırıldığı yerden verilecek, çağıran yer conf dosyasından okuyacak.

def get_data(prometheus_url, query):
  response = requests.get(prometheus_url + '/api/v1/query', params={'query': query})
  results = response.json()['data']['result']
  return results


# Bu ve altındaki fonksiyonları birleştirebiliriz.
def get_requests_from_prometheus(pod_list, prometheus_url):
    metrics = get_data(prometheus_url, 'kube_pod_container_resource_requests')

    for metric in metrics:
        pod_index = pod_list_funcs.get_pod_index(pod_list, metric['metric']['pod'])
        
        if pod_index == -1:
            pod = pod_class.Pod(metric['metric']['pod'])
            pod_list.append(pod)
            pod_index = len(pod_list) - 1

        pod_list[pod_index].set_pod_requests(metric['metric']['resource'], metric['value'][1])


def get_limits_from_prometheus(pod_list, prometheus_url):
    metrics = get_data(prometheus_url, 'kube_pod_container_resource_limits')

    for metric in metrics:
        pod_index = pod_list_funcs.get_pod_index(pod_list, metric['metric']['pod'])
        
        if pod_index == -1:
            pod = pod_class.Pod(metric['metric']['pod'])
            pod_list.append(pod)
            pod_index = len(pod_list) - 1

        pod_list[pod_index].set_pod_limits(metric['metric']['resource'], metric['value'][1])


def get_cpu_usage_from_prometheus(pod_list, prometheus_url):
    ignores = get_ignores()
    query = 'sum(irate(container_cpu_usage_seconds_total{'+ ignores +'container!=""}[2m]))by(node,pod)'
    print(query)
    metrics = get_data(prometheus_url, query)

    for metric in metrics:
        pod_index = pod_list_funcs.get_pod_index(pod_list, metric['metric']['pod'])
        
        if pod_index == -1:
            pod = pod_class.Pod(metric['metric']['pod'])
            pod_list.append(pod)
            pod_index = len(pod_list) - 1

        pod_list[pod_index].cpu_usage = metric['value'][1]


def get_memory_usage_from_prometheus(pod_list, prometheus_url):
    query = get_ignores()
    metrics = get_data(prometheus_url, 'avg(container_memory_working_set_bytes{'+ query +'pod!="",image=""})by(pod)')

    for metric in metrics:

        pod_index = pod_list_funcs.get_pod_index(pod_list, metric['metric']['pod'])
        if pod_index == -1:
            pod = pod_class.Pod(metric['metric']['pod'])
            pod_list.append(pod)
            pod_index = len(pod_list) - 1

        pod_list[pod_index].mem_usage = metric['value'][1]
        
