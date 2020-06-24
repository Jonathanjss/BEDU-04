import sys
import math

resultsList = []

def calcSquareArea():
    print('##### SQUARE AREA #####')
    side = float(input('Please enter the size of the square side: '))
    squareArea = side ** 2
    print(f'\nSquare area is {squareArea} m^2')
    print('\n\nWhat would you like to do?\n\t1) Calculate area again.\n\t2) Calculate area of another figure.\n\t3) Show results history.\n\t4) Exit.')
    functionState = 'square'
    getResults(functionState, squareArea)
    nextAction(functionState)

def calcRentangleArea():
    print('##### RECTANGLE AREA #####')
    length = float(input('Please enter the length of the rectangle: '))
    width = float(input('Please enter the width of the rectangle: '))
    rectangleArea = length * width
    print(f'\nRectangle area is {rectangleArea} m^2')
    print('\n\nWhat would you like to do?\n\t1) Calculate area again.\n\t2) Calculate area of another figure.\n\t3) Show results history.\n\t4) Exit.')
    functionState = 'rectangle'
    getResults(functionState, rectangleArea)
    nextAction(functionState)

def calcTriangleArea():
    print('##### TRIANGLE AREA #####')
    length = float(input('Please enter the length of the rectangle: '))
    base = float(input('Please enter the width of the rectangle: '))
    triangleArea = (length * base) / 2
    print(f'\nTriangle area is {triangleArea} m^2')
    print('\n\nWhat would you like to do?\n\t1) Calculate area again.\n\t2) Calculate area of another figure.\n\t3) Show results history.\n\t4) Exit.')
    functionState = 'triangle'
    getResults(functionState, triangleArea)
    nextAction(functionState)

def calcCircleArea():
    print('##### CIRCLE AREA #####')
    radius = float(input('Please enter the circle radius: '))
    circleArea = math.pi * (math.pow(radius, 2))
    print(f'\nCircle area is {circleArea} m^2')
    print('\n\nWhat would you like to do?\n\t1) Calculate area again.\n\t2) Calculate area of another figure.\n\t3) Show results history.\n\t4) Exit.')
    functionState = 'circle'
    getResults(functionState, circleArea)
    nextAction(functionState)

def nextAction(functionState):
    userSelection = int(input('Please choose an option: '))
    afterCalcArea(userSelection, functionState)

def afterCalcArea(userSelection,functionState):
    if userSelection == 1:
        if functionState == 'square':
            calcSquareArea()
        elif functionState == 'rectangle':
            calcRentangleArea()
        elif functionState == 'triangle':
            calcTriangleArea()
        elif functionState == 'circle':
            calcCircleArea()
    elif userSelection == 2:
        initApp()
    elif userSelection == 3:
        showResults()
    elif userSelection == 4:
        print("Bye")
        sys.exit()
    else:
        while True:
            userSelection = int(input('Non-valid option. Please choose a valid option: '))
            afterCalcArea(userSelection, functionState)

def getResults(figure, results):
    result = {
        "figure": figure,
        "result": results
    }
    resultsList.append(result)

def afterShowingResults(userSelection):
    if userSelection == 1:
        initApp()
    elif userSelection == 2:
        print("Bye.")
        sys.exit()
    else:
        while True:
            userSelection = int(input('Non-valid option. Please choose a valid option: '))
            afterShowingResults(userSelection)

def showResults():
    print('##### LIST OF RESULTS #####')
    print(f'{len(resultsList)} elements in the list.')
    if len(resultsList) == 0:
        print('Your result list is empty\n')
        print('\nWhat would you like to do?\n\t1) Calculate area of a figure.\n\t2) Exit.')
        userSelection = int(input('Please choose an option: '))
        afterShowingResults(userSelection)
    else:
        for result in resultsList:
            print(f'\nShape: {result["figure"]}\nArea: {result["result"]} m^2')
        print('\nWhat would you like to do?\n\t1) Calculate area of a figure.\n\t2) Exit.')
        userSelection = int(input('Please choose an option: '))
        afterShowingResults(userSelection)

def menuApp(userSelection):
    if userSelection == 1:
        calcSquareArea()
    elif userSelection == 2:
        calcRentangleArea()
    elif userSelection == 3:
        calcTriangleArea()
    elif userSelection == 4:
        calcCircleArea()
    elif userSelection == 5:
        showResults()
    elif userSelection == 6:
        print('Bye')
        sys.exit()
    else:
        return

def initApp():
    while True:
        print('Which figure would you like to calculate its area from?')
        print('\t1) Square.\n\t2) Rectangle.\n\t3) Triangle.\n\t4) Circle.\n\t5) Show results list.\n\t6) None (Exit).\n')
        userSelection = int(input('Please choose an option: '))
        menuApp(userSelection)
        while True:
            userSelection = int(input('Non-valid option. Please choose a valid option: '))
            menuApp(userSelection)

initApp()
#Lista de contactos, lista de compras y este, cuantos contactios y si estan repetidos.