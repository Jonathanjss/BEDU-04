import sys
productList = []
taxValue = 0.16

def menuApp():
  print('What would you like to do?\n\t1) Add a product.\n\t2) Show products list.\n\t3) Exit.\n')
  userSelection = int(input('Please choose an option: '))
  checkUserSelection(userSelection)

def checkUserSelection(userSelection):
  if userSelection == 1:
    addProduct()
  elif userSelection == 2:
    showProductsList()
  elif userSelection == 3:
    print('Bye.')
    sys.exit()
  else:
    userSelection = int(input('Non-valid option. Please enter a valid option: '))
    checkUserSelection(userSelection)

def addProduct():
  productName = input('Product name: ')
  productPrice = float(input('Product price: '))
  productQty = int(input('Quantity of the product: '))
  product = {
    "productName": productName,
    "productPrice": productPrice,
    "productQty": productQty,
    "totalPrice": (productPrice + (productPrice * taxValue)) * productQty
  }
  productList.append(product)
  print('\nPRODUCT ADDED TO THE LIST!\n')
  print('What would you like to do?\n\t1) Add other product.\n\t2) Show product list.\n\t3) Exit.\n')
  userSelection = int(input('Please choose an option: '))
  checkUserSelection(userSelection)

def showProductsList():
  if len(productList) == 0:
    print('\nYour list is empty :(\n')
    menuApp()
  else:
    totalPrice = 0
    totalQty = 0
    print('\n----------PRODUCTS----------')
    for product in productList:
      for productIndex in product.keys():
        if productIndex == 'productName':
          print(f'Name: {product[productIndex]}')
        elif productIndex == 'productPrice':
          print(f'Price: {product[productIndex]}')
        elif productIndex == 'productQty':
          totalQty += product[productIndex]
          print(f'Qty: {product[productIndex]}')
        else:
          totalPrice += product[productIndex]
          print(f'Total with taxes: {product[productIndex]}\n----------------------------')
    print(f'You have {totalQty} products in your list.\nMount of these products is {totalPrice}\n')
    menuApp()

menuApp()