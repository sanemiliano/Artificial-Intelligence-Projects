from textblob import TextBlob
import nltk
import tweepy
import numpy
import pandas

daysAhead = 3
##Establishing connection with Twitter
consumerKey = "4M1JLs8JPk3HlI4EdatE94vxD"
consumenSecret = "XXMnG8qBRE5bpP9fTrcWk8HmPiEaPZSW0IxXCJviXGICRMD1nf"
accessToken = "808752852919287808-VfPDClYO4gx1AVa9G0odqUyfofdTvVG"
accessTokenSecret = "TKoZEdtweG5LnlCIINLy4sZ77EzJBAFpDUvXHUzhZtbFo"

authentication = tweepy.OAuthHandler(consumerKey,consumenSecret)
authentication.set_access_token(accessToken,accessTokenSecret)

API = tweepy.API(authentication)

tweets = API.search('tesla')

results = []

for tweet in tweets:
    results.append(TextBlob(tweet.text).sentiment)

numpy.savetxt("TwitterResults.csv", results, delimiter=",")

results = pandas.read_csv("TwitterResults.csv",delimiter=",")
results
sum = 0.0
for result in results:
    sum = sum + float(result)

print(sum)