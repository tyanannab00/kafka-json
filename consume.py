from kafka import KafkaConsumer
import json

if __name__ == "__main__":
    consumer = KafkaConsumer(
        "20211215",
        bootstrap_servers='localhost:9092',
        auto_offset_reset='earliest',
        group_id="consumer-group-a")
    print("starting the consumer")
    for msg in consumer:
        print("Data = {}".format(json.loads(msg.value)))


        message = json.loads(msg.value)
        print(message['identity'][0]['name'])