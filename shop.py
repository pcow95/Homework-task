import json

#Welcome to shop, create shop stock dict

customer_funds = 100
purchase = []
shop_items =  {

  "item1" : {
    "name" : 'bicycle',
    "item_price" : 101
  },
  "item2" : {
    "name" : 'trainers',
    "item_price" : 40
  },
  "item3" : {
    "name" : 'socks',
    "item_price" : 10
  },
  "item4" : {
    "name": 'maps',
    "item_price" : 4
  }
}
# Customer Welcomed to shop and shown items

print("Welcome to my shop, here are the items and prices", json.dumps(shop_items, indent=0))

# Customer offered to exit or continue

while progress := input("Please type 'continue' to proceed, or 'exit' to quit...").lower():

    if progress == 'exit':
        raise ValueError("You have left the shop, see you again soon")

    elif progress == 'continue':
        purchase = (input("Let's shop! Press enter"))
        break
    else: raise ValueError("Please choose continue or exit")

#Customer views shop items and chooses one for purchase

while True:
    customer_funds = int(100)
    name = shop_items.get("name")
    item_price = shop_items.get("price")
    try:
        print(shop_items.values())
        purchase = str(input("What would you like to buy?")).lower()

    except ValueError:
        print("Please make a valid selection")

#Customer attempts purchase and recieves outcome

    while purchase in shop_items:
        if 100 > item_price:
            print("Purchase success, here is your item. See you soon!")
    else:
            print("Sorry, that didn't go through.")
            answer = input(" Do you have more money? (Yes/No)").lower()

#Funds are added to the customer's wallet

    if answer == ('yes'):
        add_cash = (int(input("How much would you like to add?")))
        customer_funds = 100
        print("Total funds", customer_funds + add_cash, "... let's try again!")
        new_funds = (customer_funds + add_cash)

    else: raise ValueError("Sorry, you have insufficient funds. Come back soon")

#Purchase is reattempted 3 times with new funds

    for x in range(3):
       try:
           if new_funds >= 101:
               print("Purchase success, here is your item. See you soon!")
       except: raise ValueError("Sorry, that didn't work")
    break

