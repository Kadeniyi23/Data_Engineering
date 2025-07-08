from kafka import KafkaProducer

# Create Message
msg = 'Hi My name is Adeniyi kabirat'

# Create a producer
producer = KafkaProducer(bootstrap_servers='localhost:9092')


# Function to send messages into Kafka
def kafka_python_producer_async(producer, msg):
    producer.send('initialtopic', msg).add_callback(success).add_errback(error)
    producer.flush()

    print(msg)


def success(metadata):
    print(metadata.topic)


def error(exception):
    print(exception)


print("start producing")

#Seriailizing into bytes
# kafka_python_producer_async(producer, bytes(msg, 'utf-8'))

print("done")
