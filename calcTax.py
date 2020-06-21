stateValue = True
productsList = []
taxValue = 0.16

def addProduct():
  name = input("Enter product name: ")
  price = float(input("Enter product price: "))
  quantity = int(input("Enter quantity of this product: "))
  product = {
    "name" : name,
    "price" : price,
    "quantity" : quantity,
    "total": (price + (price*taxValue)) * quantity
  }
  productsList.append(product)

def printProducts():
  qtyTotal = 0
  priceTotal = 0
  print(f'\n\nYour products list: \n')
  for element in productsList:
    qtyTotal += element["quantity"]
    priceTotal += element["total"]
    print(f'Product Name: {element["name"]}\nTax-free price: {element["price"]}\nQuantity: {element["quantity"]}\nTotal: {element["total"]}\n\n')
  print(f'Total of products you bought {qtyTotal}\nTotal to be paid is {priceTotal}')

while stateValue:
  decision = input("Would you like to add a product? Yes/No: ")
  decision = decision.lower()
  if decision == "yes":
    addProduct()
  elif decision == "no":
    printProducts()
    stateValue = False
  else:
    print('That\'s not a valid answer. Try again\n')
    continue