import config


class Pod:
    cpu_req = ""
    cpu_limit = ""
    cpu_usage = ""
    mem_req = ""
    mem_limit = ""
    mem_usage = ""
  

    def __init__(self, pod_name, cluster = config.CLUSTER_NAME):
        self.pod_name = pod_name
        self.cluster = cluster
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