import sys
contactList = []
def initApp():
    while True:
        print('Menu: \n\t1) Show contacts.\n\t2) Add contact.\n\t3) Delete contact.\n\t4) Show contact details.\n\t5) Exit.')
        userOption = int(input('Please choose an option: '))
        if userOption == 1:
            showContacts()
        elif userOption == 2:
            addContact()
        elif userOption == 3:
            deleteContact()
        elif userOption == 4:
            showContactDetails()
        elif userOption == 5:
            print('Bye')
            sys.exit()
        else:
            print('Option not valid')

def showContacts():
    counter = 1
    if len(contactList) == 0:
        print('\nYour contact list is empty :(\n')
        initApp()
    else:
        print('#### CONTACT LIST ####')
        for contact in contactList:
            print(f'{counter}.- {contact["name"]}')
            counter += 1
    while True:
        print('\n')
        initApp()

def addContact():
    print('#### ADD CONTACT ####')
    print("Please enter the following contact info.")
    contactName = input('Name: ')
    contactEmail = input('Email: ')
    contactPhone = input('Phone number: ')
    contact = {
        "name": contactName,
        "email": contactEmail,
        "phone": contactPhone
    }
    contactList.append(contact)
    print('Contact added!')
    while True:
        userDecision = input('Would you like to add another contact?(Y/N)  ')
        userDecision = userDecision.lower()
        if userDecision == "y":
            addContact()
        elif userDecision == "n":
            initApp()
        else:
            print('Non-valid option. Press "y" for yes OR "n" for no')

def deleteContact():
    counter = 1
    if len(contactList) == 0:
        print('\nYour contact list is empty :(\n')
        initApp()
    else:
        print('#### CONTACT LIST ####')
        for contact in contactList:
            print(f'{counter}.- {contact["name"]}')
            counter += 1
        while True:
            userOption = int(input('Select user to be deleted  '))
            if userOption <= len(contactList):
                userDeleted = contactList.pop(userOption - 1)
                print(f'\n{userDeleted["name"]} was deleted from your contact list.\n')
                while True:
                    print('1) Delete another contact.\n2) Go to the menu.')
                    userOption = int(input('Please choose an option: '))
                    if userOption == 1:
                        deleteContact()
                    elif userOption == 2:
                        initApp()
                    else:
                        print('Non-valid option.')
            else:
                print('This contact doesn\'t exist.')

def showContactDetails():
    counter = 1
    if len(contactList) == 0:
        print('\nYour contact list is empty :(\n')
        initApp()
    else:
        print('#### CONTACT LIST ####')
        for contact in contactList:
            print(f'{counter}.- {contact["name"]}')
            counter += 1
        while True:
            userOption = int(input('Which user do you want to see information about?: '))
            if userOption <= len(contactList):
                print('\n#### CONTACT INFO ####')
                print(f'Name:{contactList[userOption-1]["name"]}\nEmail:{contactList[userOption-1]["email"]}\nPhone:{contactList[userOption-1]["phone"]}\n')
                while True:
                    print('1) View the info of another contact.\n2) Go to the menu.')
                    userOption = int(input('Please choose an option: '))
                    if userOption == 1:
                        showContactDetails()
                    elif userOption == 2:
                        initApp()
                    else:
                        print('Non-valid option.')
            else:
                print('User selected doesn\'t exist.')

initApp()
