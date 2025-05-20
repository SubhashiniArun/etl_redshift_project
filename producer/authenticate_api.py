# import boto3
import os
import tweepy
from dotenv import load_dotenv

load_dotenv()

def authenticate_twitter():
    # API_KEY = os.getenv("twitter_api_key")
    # API_SECRET_KEY = os.getenv("twitter_api_secret_key")
    # ACCESS_TOKEN = os.getenv("twitter_access_token")
    # ACCESS_TOKEN_SECRET = os.getenv("twitter_token_secret")

    # auth = tweepy.OAuth1UserHandler(consumer_key=API_KEY, consumer_secret=API_SECRET_KEY, 
    #                             access_token=ACCESS_TOKEN, access_token_secret=ACCESS_TOKEN_SECRET)
    # print(f"Twitter API authenticated {auth}")
    # api = tweepy.API(auth)

    # print(f"Twitter API {api}")

    client = tweepy.Client(bearer_token=os.getenv('twitter_bearer_token'))

    return client

def authenticate_weatherstack():
    WEATHER_STACK_KEY = os.getenv("weatherstack_api_key")
    external_url = f'http://api.weatherstack.com/current?access_key={WEATHER_STACK_KEY}&query=New York;'
    return external_url