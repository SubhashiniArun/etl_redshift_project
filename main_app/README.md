# ETL / Asynchronous Processing
Pipeline integrates with the external API
Solves of the problem of tight coupling between the systems and reduces load on the server by processing the data in batches

# Producer APP
-> Pipeline that is automated to run every day afternoon 2 PM will load the external data 
-> send the fetched data to RabbitMQ (port: 15672) for batch processing

# Consumer APP
-> Consumer listens to the queue 'batch-queue'
-> fetches the message/data from RabbitMQ (port: 15672) when a message gets added to the queue
-> Load the message/data into Redshift table

# Technologies
-> RabbitMQ (port: 15672) for queing the message
-> Producer that pushes messages to queue is automated using cron job

-> @app.before_request decorator starts the consumer thread
-> consumer listens to queue runs on the port 5000 as as separate thread (threading.Thread(target=consume_batch)). Thread daemon terminates when the main program exits
-> consumer connects to RabbitMQ (port: 15672)  
-> process the message and load into the Redshift table synchronously within the thread

