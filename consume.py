from kafka import KafkaConsumer
import json

if __name__ == "__main__":
    consumer = KafkaConsumer(
        "latihan-jumat",
        bootstrap_servers='localhost:9092',
        auto_offset_reset='earliest',
        group_id="consumer-group-c")
    print("starting the consumer")
    for msg in consumer:
        print("Data = {}".format(json.loads(msg.value)))