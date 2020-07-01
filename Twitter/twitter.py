from tweet import Tweet

class Twitter():
    def __init__(self):
        self.tweets = [] # List of tweets.

    def print_timeline(self):
        for tweet in self.tweets:
            print(f'{tweet.print_twitter_format()}')