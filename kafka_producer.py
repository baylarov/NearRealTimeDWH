import time, requests
import json
from kafka import KafkaProducer

bts_server = ["localhost:9092"]
topic = "sparking"
val_serialize = lambda x: json.dumps(x).encode('utf-8')

producer = KafkaProducer(bootstrap_servers=bts_server, value_serializer=val_serialize)

id = 48
while id <= 55:
    url = 'http://127.0.0.1:5000/employees/{}'.format(id)
    response = requests.get(url, verify=False, timeout=180)
    result = response.json()
    producer.send(topic=topic, value=result)
    print("'{}' has been sent to the topic '{}'".format(result,topic))
    time.sleep(10)
    id += 1
