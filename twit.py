import sys
from datetime import datetime

usersList = []

class User():
    def __init__(self, name, birthDate, registrationDate, location):
        self.name = name
        self.birthDate = birthDate
        self.registrationDate = registrationDate
        self.location = location

class tweet():
    def __init__(self, text, creationDate, updateDate):
        self.text = text
        self.creationDate = creationDate
        self.updateDate = updateDate
        self.likes = 0
        self.retweets = 0

    def giveLike(self):
        self.likes += 1

    def giveRetweet(self):
        self.retweets += 1

def menuApp():
    print('\nWhat would you like to do?\n\t1) Register.\n\t2) Show users.\n\t3) Exit.\n')
    userSelection = int(input('Please choose an option: '))
    checkUserSelection(userSelection)

def checkUserSelection(userSelection):
    if userSelection == 1:
        funcRegister()
    elif userSelection == 2:
        showUsers()
    elif userSelection == 3:
        print('\nBye!')
        sys.exit()
    else:
        userSelection = int(input('Non-valid option. Please choose a valid option: '))
        checkUserSelection(userSelection)

def funcRegister():
    name = input('Username: ')
    birthDate = input('Birthdate (dd/mm/yyy): ')
    registrationDate = datetime.now()
    registrationDate = registrationDate.strftime("%d/%m/%Y %H:%M:%S")
    location = input('Location: ')
    user_dic = {
        "name": name,
        "birthDate": birthDate,
        "registrationDate": registrationDate,
        "location": location
    }
    a = User(**user_dic)
    usersList.append(a)
    menuApp()

def showUsers():
    if len(usersList) == 0:
        print('Empty list.')
        menuApp()
    else:
        for user in usersList:
            print(f'\nusername: {user.name}\nbirthdate: {user.birthDate}\nlocation: {user.location}\nmember since: {user.registrationDate}')
        menuApp()

menuApp()

