import random
import sys

resultsHistory = {
    "counter": 0,
    "1": 0,
    "2": 0,
    "3": 0,
    "4": 0,
    "5": 0,
    "6": 0
}

def getThrowHistory(diceResult):
    if diceResult == 1:
        resultsHistory["1"] += 1
        resultsHistory["counter"] += 1
    elif diceResult == 2:
        resultsHistory["2"] += 1
        resultsHistory["counter"] += 1
    elif diceResult == 3:
        resultsHistory["3"] += 1
        resultsHistory["counter"] += 1
    elif diceResult == 4:
        resultsHistory["4"] += 1
        resultsHistory["counter"] += 1
    elif diceResult == 5:
        resultsHistory["5"] += 1
        resultsHistory["counter"] += 1
    else:
        resultsHistory["6"] += 1
        resultsHistory["counter"] += 1

def showThrowHistory():
    if resultsHistory["counter"] == 0:
        print('There are not values in the list.')
    else:
        print(f'\nYou threw the dice {resultsHistory["counter"]} times, where:')
        for result in resultsHistory.keys():
            if result == 'counter':
                continue
            elif resultsHistory[result] > 0:
                percentage = (resultsHistory[result] * 100)/resultsHistory['counter']
                print(f'You got {resultsHistory[result]} times the number {result} ({percentage}%).')
    menuApp()

def rollDice():
    diceResult = random.randint(1, 6)
    print(f'\nResult of the dice threw: {diceResult}')
    getThrowHistory(diceResult)
    menuApp()

def checkSelection(userSelection):
    if userSelection == 1:
        rollDice()
    elif userSelection == 2:
        showThrowHistory()
    elif userSelection == 3:
        print('\nBye.')
        sys.exit()
    else:
        while True:
            userSelection = int(input('Non-valid option. Please choose an option: '))
            checkSelection(userSelection)

def menuApp():
    print('\nPlease choose an option:\n\t1) Roll the dice.\n\t2) View stadistics.\n\t3) Exit.')
    userSelection = int(input('Please choose an option: '))
    checkSelection(userSelection)

menuApp()
