#!/usr/bin/python3

from dotenv import load_dotenv
from time import sleep
import os
import tweepy

#https://www.geeksforgeeks.org/python-status-object-in-tweepy/

load_dotenv()

def main():
    client = tweepy.Client(bearer_token = os.getenv("BEARER_TOKEN"),
                               access_token = os.getenv("API_KEY"),
                               access_token_secret = os.getenv("API_SECRET"))

    query="monke -is:retweet"
    tweets = client.search_recent_tweets(query=query,
                                         tweet_fields = ["created_at", "text", "source"],
                                         user_fields = ["name", "username", "location", "verified", "description"],
                                         max_results = 10,
                                         expansions='author_id'
                                         )
    searched_tweet_data = tweets.data

    for x in range(0,len(searched_tweet_data)):
        text=searched_tweet_data[x].text.replace('\n','\n\t')
        user=tweets.includes["users"][x].name
        print(f"Who> @{user}\ntweet_id> {searched_tweet_data[x].id}\n\t{text}")
        print('\n\t==========\n')


if __name__ == '__main__':
    main()
