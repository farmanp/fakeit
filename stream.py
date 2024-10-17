from faker import Faker
from confluent_kafka import Producer
import json
import time

fake = Faker()

producer_config = {
    'bootstrap.servers': 'localhost:9092'  # Kafka broker address
}
producer = Producer(producer_config)

def delivery_report(err, msg):
    """Callback for message delivery report."""
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))

def generate_event():
    """Generate a fake event to be streamed."""
    return {
        'name': fake.name(),
        'email': fake.email(),
        'address': fake.address(),
        'timestamp': time.time()
    }

def stream_events(topic, num_events=100, interval=1):
    for _ in range(num_events):
        event = generate_event()
        producer.produce(topic, key=str(fake.uuid4()), value=json.dumps(event), callback=delivery_report)
        producer.poll(0)
        time.sleep(interval)

if __name__ == "__main__":
    stream_events(topic='faker_topic', num_events=50, interval=2)
