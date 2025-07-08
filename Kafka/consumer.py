from kafka import KafkaConsumer

consumer = KafkaConsumer()

#define a consumer that waits for messages

def kafka_consumer():
    consumer=KafkaConsumer('initialtopic',bootstrap_servers=['localhost:9092'],group_id='initial_grouping')

    for message in consumer:
        print(message)

print("consumption has started")

kafka_consumer()

print("consumption has ended")


