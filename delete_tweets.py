import twitter

api = twitter.Api(consumer_key='',
                  consumer_secret='',
                  access_token_key='',
                  access_token_secret='')

timeline = api.GetUserTimeline(screen_name='')

for tweet in timeline:
    print(tweet)
    try:
        api.DestroyStatus(tweet.id)
    except Exception as e:
        print(e.args)