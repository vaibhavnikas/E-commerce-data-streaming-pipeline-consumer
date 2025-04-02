from dotenv import dotenv_values
import json
from kafka_consumer import create_kafka_consumer, consume_messages
from postgres_connector import PostgresDB
from utilities import get_date_dimensions


config = dotenv_values('.env')

bootstrap_servers = json.loads(config['BOOTSTRAP_SERVERS'])
consumer = create_kafka_consumer(bootstrap_servers, 'e-commerce-transactions')

db = PostgresDB(
    host = config['PG_HOST'],
    port = config['PG_PORT'],
    db = config['SALES_DB'],
    user = config['PG_USER'],
    pw = config['PG_PASS']
)

for message in consume_messages(consumer):
    if message['type'] == 'transaction':
        transaction_data = message['transaction_data']
        data = []
        for record in transaction_data:
            data.append(tuple(record.values()))
        db.writemany('fact_transaction', data)
    elif message['type'] == 'date':
        data = get_date_dimensions(message)
        db.write('dim_date', data)
