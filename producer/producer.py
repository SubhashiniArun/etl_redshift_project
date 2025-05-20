import pika
import json
import tweepy
import os
import requests
# import pandas as pd

from authenticate_api import authenticate_weatherstack

# twitter_api_key = "XoMLNpCrs7xgNlh6hqxZjk6aN"
# twitter_api_secret_key = "gWv4FNF5pd3sn6tmGAk9yuw13M0sCCN1zsrlW2pIwxg6xEK6jg"
# twitter_access_token = "2251685090-Kz4I4Xkoe1lV4ZMxBWE0woceRzufCqgBM6hI8IL"
# twitter_token_secret = "ZZIpkFHrLQP2mkPc3YY6SXmeDFYsjH9b695t1vfeU3J1i"

API_KEY = os.getenv("twitter_api_key")
API_SECRET_KEY = os.getenv("twitter_api_secret_key")
ACCESS_TOKEN = os.getenv("twitter_access_token")
ACCESS_TOKEN_SECRET = os.getenv("twitter_token_secret")

auth = tweepy.OAuth1UserHandler(consumer_key=API_KEY, consumer_secret=API_SECRET_KEY, 
                                access_token=ACCESS_TOKEN, access_token_secret=ACCESS_TOKEN_SECRET)
print(f"Twitter API authenticated {auth}")
api = tweepy.API(auth)

print(f"Twitter API {api}")

def fetch_click_metrics():
    # Example: Fetching tweets with engagement data (e.g., click metrics)
    tweets = api.user_timeline(screen_name='@JOhn', count=10)
    click_metrics = []

    for tweet in tweets:
        click_metrics.append({
            'tweet_id': tweet.id,
            'created_at': tweet.created_at,
            'clicks': tweet.favorite_count,  # Example metric: likes as clicks
            'retweets': tweet.retweet_count
        })
    
    return click_metrics


def fetch_external_api_data():
    weatherstack_url = authenticate_weatherstack()
    response = requests.get(weatherstack_url)
    current_data = response.json()['current']['astro']
    # print(f"current astro data {current_data}")
    # df = pd.DataFrame(current_data, index=[0])
    # print(f"DF {df}")
    # print(df.info())
    return current_data

def publish_batch(batch_data):
    # Connecting to RabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    channel = connection.channel()

    print(f"Channel: {channel}")

    # Declare the queue (in case it doesn't exist)
    channel.queue_declare(queue="batch-queue")

    # Publish each message in the batch to queue
    for item in batch_data:
        channel.basic_publish(exchange='',
                            routing_key="batch_queue",
                            body=json.dumps(item)
                            )
    print(f"Sent {len(batch_data)} messages to the queue")

    # Close connection
    connection.close()

def run_pipeline():
    api_data = fetch_external_api_data()
    print(f"click metrics {api_data}")
    batch_data = [api_data]
    publish_batch(batch_data)


if __name__ == "__main__":
    run_pipeline()