from kafka import KafkaProducer
import json
# from data import get_registered_user
import time

with open('sample.json', 'r') as openfile:
    json_object = json.load(openfile)

def json_serializer(data):
    return json.dumps(data).encode("utf-8")


producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=json_serializer)


if __name__ == "__main__":
        # registered_user = get_registered_user()
        # print(registered_user)
        producer.send("20211215", json_object)
        time.sleep(4)

