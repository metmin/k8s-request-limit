def get_pod_index(pod_list, pod_name, cluster_name, team_name):
    index = 0
    for pod in pod_list:
        if pod.pod_name == pod_name and pod.cluster_name == cluster_name and pod.team_name == team_name:
            return index
        index = index + 1
    return -1


def calculate_diff(pod_list):
    error_message = ""

    diff_list = {}

    for pod in pod_list:
        if pod.cpu_req == "" or pod.mem_req == "" or pod.cpu_usage == "0" or pod.cpu_usage == "":
            error_message += f"```There is an error about {pod.team_name}/{pod.cluster_name}/{pod.pod_name} cpu or memory request```\n"
            continue

        cpu_req   = float(pod.cpu_req)
        cpu_usage = float(pod.cpu_usage)
        mem_req   = int(pod.mem_req)   / 1024 / 1024
        mem_usage = int(pod.mem_usage) / 1024 / 1024
        
        # abs(usage - request) / usage * 100  
        cpu_diff =  abs(cpu_usage - cpu_req) / cpu_usage * 100
        mem_diff =  abs(mem_usage - mem_req) / mem_usage * 100

        if cpu_diff > 15000 or mem_diff > 15000:

            if pod.team_name not in diff_list:
                diff_list[pod.team_name] = []

            diff_list[pod.team_name].append(
                {
                    "cluster"   : pod.cluster_name,
                    "pod"       : pod.pod_name,
                    "cpu_req"   : pod.cpu_req,
                    "cpu_usage" : pod.cpu_usage,
                    "cpu_diff"  : cpu_diff,
                    "mem_req"   : pod.mem_req,
                    "mem_usage" : pod.mem_usage,
                    "mem_diff"  : mem_diff,
                })

    return diff_list
