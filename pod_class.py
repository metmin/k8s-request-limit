import config
import slack_api

class Pod:
    cpu_req   = ""
    cpu_limit = ""
    cpu_usage = ""
    mem_req   = ""
    mem_limit = ""
    mem_usage = ""

    
    def __init__(self, pod_name, cluster = config.CLUSTER_NAME):
        self.pod_name = pod_name
        self.cluster  = cluster
        '''
        self.cpu_req = cpu_req
        self.cpu_limit = cpu_limit
        self.cpu_usage = cpu_usage
        self.mem_req = mem_req
        self.mem_limit = mem_limit
        self.mem_usage = mem_usage
        '''


    def set_pod_requests(self, resource, value):
        if resource == 'cpu':
            self.cpu_req = value
        elif resource == 'memory':
            self.mem_req = value


    def set_pod_limits(self, resource, value):
        if resource == 'cpu':
            self.cpu_limit = value
        elif resource == 'memory':
            self.mem_limit = value


    def get_pod_index(pod_list, pod_name):
        index = 0
        for pod in pod_list:
            if pod.pod_name == pod_name:
                return index
            index = index + 1
        
        return -1
    
    
    @staticmethod
    def calculate_cpu_diff(pod_list):
  
        for pod in pod_list:

            if pod.cpu_req == "" or pod.mem_req == "" or pod.cpu_usage == "0":
            # TODO: Slack kanalına ayarlanmadığı ile ilgili mesaj göndersin. - DONE
            # TODO: cpu kullanımı 0'sa da mesaj basabilir. 
                slack_api.send_error_notification(config.WEBHOOK_URL, pod)
                continue

            cpu_req   = float(pod.cpu_req)
            cpu_usage = float(pod.cpu_usage)
            mem_req   = int(pod.mem_req)   / 1024 / 1024
            mem_usage = int(pod.mem_usage) / 1024 / 1024
            
            #Formula: |usage - request| / usage * 100  
            cpu_diff =  abs(cpu_usage - cpu_req) / cpu_usage * 100
            mem_diff =  abs(mem_usage - mem_req) / mem_usage * 100

            if cpu_diff > 10000 or mem_diff > 150:
                slack_api.send_diff_notification(config.WEBHOOK_URL, pod, cpu_diff, mem_diff)
