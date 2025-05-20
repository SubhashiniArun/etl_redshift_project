import threading
import pika
import json
import time

from Redshift.redshift_connection import redshift_connection

database_name = 'dev'
workgroup_name = 'default-workgroup'

def process_message(message):
    time.sleep(1) # Simulate the time taken to process a message
    conn = redshift_connection()
    print(f" Redshift Connection established with consumer {conn}")
    print(f"Process MESSAGE {message}")
    print("Executing Statement")

    load_sql_statement = f"""INSERT INTO astro_data (sunrise, sunset, moonrise, moonset, moon_phase, moon_illumination) VALUES ('{message['sunrise']}', '{message['sunset']}', '{message['moonrise']}', '{message['moonset']}', '{message['moon_phase']}', '{message['moon_illumination']}')"""
    
    load_response = conn.execute_statement(
            Database=database_name,
            WorkgroupName=workgroup_name,
            Sql=load_sql_statement
        )
    print(f"sql_statement response insert into table {load_response}")


    # paginator = conn.get_paginator('get_statement_result')

    # response_iterator = paginator.paginate(
    #     Id='278e706a-d9f2-4907-891d-4189a0d028d6',
    #     # Database='dev',
    #     # WorkgroupName="dev-workgroup",
    #     # Table='tasks',
    # )
    # print(f"sql_statementttt resulttttttt 2221 {response_iterator}")
    # for item in response_iterator:
    #     print(f"item {item}")

    # # response = conn.list_tables(
    # #     Database='dev',
    # #     WorkgroupName="dev-workgroup",
    # #     SchemaPattern="batch_processing",
    # #     TablePattern="tasks"
    # # )
    # # print(f"sql_statement response 2 {response}")
    # print(f"Processed message: {message}")

def consume_batch():
    def callback(ch, method, properties, body):
        print(f"ch {ch}")
        print(f"method {method}")
        print(f"properties {properties}")
        print(f"body {body}")
        message = json.loads(body)
        process_message(message) # process message synchronously (within this thread)

    print("Trying to establish Connection...")
    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    print("Connection Established...")
    channel = connection.channel()
    print("Channel connection created...")
    channel.queue_declare(queue="batch_queue")
    print("Queue declared...")

    # start consuming the messages from the queue
    channel.basic_consume(queue="batch_queue",
                          on_message_callback=callback,
                          auto_ack=True)
    print("Started consuming messages...")
    channel.start_consuming()

# Start the consumer in a separate thread
def start_consumer_thread():
    consumer_thread = threading.Thread(target=consume_batch)
    print("Consumer thread created.")
    consumer_thread.daemon = True # Ensure that the thread stops when the main program exists
    print("Consumer thread daemon set.")
    consumer_thread.start()
    print("Consumer thread started.")


