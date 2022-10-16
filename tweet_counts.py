import tweepy

client = tweepy.Client(bearer_token='')  #insert your own token here

# Replace with your own search query
query = '#BBNaija -is:retweet lang:en'

counts = client.get_recent_tweets_count(query=query, end_time='2022-10-01T00:00:00.000Z', granularity='day', start_time='2022-09-28T00:00:00.000Z')

for count in counts.data:
    print(count)
    