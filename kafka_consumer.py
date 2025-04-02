from kafka import KafkaConsumer
import json


def create_kafka_consumer(bootstrap_servers, topic):
    try:
        consumer = KafkaConsumer(
            topic,
            bootstrap_servers=bootstrap_servers,
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            value_deserializer=lambda v: json.loads(v.decode('utf-8'))
        )
        return consumer
    except Exception as e:
        print(f"Error creating Kafka consumer: {e}")
        return None
    

def consume_messages(consumer):
    if consumer:
        try:
            for message in consumer:
                yield message.value
        except KeyboardInterrupt:
            print('Consumer stopped by user')
        except Exception as e:
            print(f"Error consuming messages: {e}")
    else:
        print('Consumer not initialized')

def close_consumer(consumer):
    if consumer:
        consumer.close()
        print("Consumer closed")