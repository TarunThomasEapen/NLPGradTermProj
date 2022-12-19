import tweepy
import csv

if __name__ == '__main__':

    client = tweepy.Client(
        bearer_token='AAAAAAAAAAAAAAAAAAAAAEOgkQEAAAAAMN8lo4Oqnm6up9VgAJNXV6ywEtM%3D8tF5k7409ZpQIIGKCsfurpifug2AyapmWT7ayxm8FTI0btUsfr')

    # query = '#UnitedAirlines -#planefence -#AvGeek lang:en -is:retweet'
    # query = '#ChatGPT lang:en -is:retweet'
    query = '#WorldCup lang:en -is:retweet'

    tweets = client.search_recent_tweets(query=query, tweet_fields=['context_annotations', 'created_at'],
                                         max_results=20)
    # Open/Create a file to append data
    # csvFile = open('UnitedAirlinesTweets.csv', 'a')
    # csvFile = open('ChatGPTTweets.csv', 'a')
    csvFile = open('Data files/WorldCupTweets.csv', 'a')

    # Use csv Writer
    csvWriter = csv.writer(csvFile)

    count = 1
    for tweet in tweets.data:
        csvWriter.writerow([count, tweet.text])
        count = count + 1
