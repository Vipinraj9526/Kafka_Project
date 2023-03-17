import requests
from time import sleep
from json import dumps
from kafka import KafkaProducer


producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))


def get_stream(url):
    s = requests.Session()

    with s.get(url, headers=None, stream=True) as resp:
        for line in resp.iter_lines():
            if line :
                print(line.decode())
                producer.send('DemoTopic4', value=line.decode())
                sleep(5)

url = 'https://stream.wikimedia.org/v2/stream/recentchange'
get_stream(url)
