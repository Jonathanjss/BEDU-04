from datetime import datetime

class Tweet():
    def __init__(self, text, author):
        # Instanced variables
        self.text = text
        self.author = author
        # Internal properties
        self.created_at = datetime.now()
        self.likes = 0
        self.retweets = 0

    @property
    def published_at(self):
        return self.created_at.strftime('%b %d, %Y')

    def add_like(self):
        self.likes += 1

    def add_retweet(self):
        self.retweets += 1

    def print_twitter_format(self):
        return f'''
        {self.author} · {self.published_at}
        {self.text}
        '''