class Pod:
    cpu_req = ""
    cpu_limit = ""
    cpu_usage = ""
    mem_req = ""
    mem_limit = ""
    mem_usage = ""
  

    def __init__(self, pod_name, cluster_name, team_name):
        self.pod_name = pod_name
        self.cluster_name = cluster_name
        self.team_name = team_name


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