import sys
from tweet import Tweet
from twitter import Twitter
from users import User
from twitterUsers import twitterUsers

twitter_user_list = twitterUsers()
tweet_user_list = Twitter()

def menuApp():
    print('Select an option:\n\t1) Register.\n\t2) Show users registered.\n\t3) Select an user and tweet something.\n\t4) Show timeline.\n\t5) Exit.')
    user_option_selected = int(input('Option: '))
    validate_option_selected(user_option_selected)

def validate_option_selected(user_option_selected):
    if user_option_selected == 1:
        register_user()
    elif user_option_selected == 2:
        show_users()
    elif user_option_selected == 3:
        select_user_tweet()
    elif user_option_selected == 4:
        show_timeline()
    elif user_option_selected == 5:
        print('Bye!')
        sys.exit()
    else:
        user_option_selected = int(input('Non-valid option. Enter a valid option please: '))
        validate_option_selected(user_option_selected)

def register_user():
    name = input('Name: ')
    birthdate = input('Birthdate (dd/mm/yyyy): ')
    location = input('Location: ')
    user = User(name, birthdate, location)
    twitter_user_list.userList.append(user)
    print('User added successfully\n')
    menuApp()

def show_users():
    twitter_user_list.print_user_list()
    menuApp()

def select_user_tweet():
    if len(twitter_user_list.userList) == 0:
        print('User list is empty.')
    else:
        print('--- USER LIST ---')
        twitter_user_list.print_user_name()
        user_option_selected = int(input('Select an user (number): '))
        user_tweet_text = input('What\'s on your mind?: ')
        user_tweet = Tweet(user_tweet_text, twitter_user_list.userList[user_option_selected-1].name)
        tweet_user_list.tweets.append(user_tweet)
        print(user_tweet.print_twitter_format())
        menuApp()

def show_timeline():
    tweet_user_list.print_timeline()
    menuApp()

menuApp()