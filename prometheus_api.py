import requests

def get_data(prometheus_url, query):
  response = requests.get(prometheus_url + '/api/v1/query', params={'query': query})
  results = response.json()['data']['result']

  return results