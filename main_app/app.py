from flask import Flask
from Consumer.consumer import start_consumer_thread

# setting up the Flask app
app = Flask(__name__)


@app.before_request
def before_first_request():
    print("Start Rabbitmq consumer thread")
    start_consumer_thread()

# declaring routes
@app.route('/')
def index():
    return "RabbitMQ Batch Processing with Flask and Parallel Consumers"

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True, use_reloader=False)  # Use reloader=False to prevent multiple instances