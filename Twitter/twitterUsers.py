from users import User

class twitterUsers():
    def __init__(self):
        self.userList = []

    def print_user_list(self):
        for user in self.userList:
            print(user.print_user())

    def print_user_name(self):
        counter = 0
        for user in self.userList:
            counter += 1
            print(f'{counter}) {user.print_user_name()}')
