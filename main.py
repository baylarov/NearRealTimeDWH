import requests
import time

id = 47
while id <= 55:
    url = 'http://127.0.0.1:5000/employees/{}'.format(id)
    response = requests.get(url, verify=False, timeout=180)
    result = response.json()
    print(result)
    time.sleep(2)
    id += 1