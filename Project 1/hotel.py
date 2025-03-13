menu ={
    'Pizza':40,
    'Pasta': 30,
    'Burger':50,
    'Salad': 44,
    'Tea':10,
}
print( "Welcome to Hotel .\nThere are our menu would you like any order  " )
print( "Pizza: Tk 40\nPasta: Tk30\nBurger: Tk 50\nSalad: Tk 44\nTea: Tk 10")

order_total = 0

item_1 = input(" Enter the name of item you want to orderb = ")

if item_1 in menu: 
    order_total += menu[item_1]
    print(f"Your item {item_1} has been Added to your order")


else:
    print(f"Ordered item {item_1} is not avaialable yet")


another_order = input ("Do you like to add another item ? (Yes/No)")
if another_order =="Yes" :
    item_2 = input(" Enter the name of second item = ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item {item_2} has been added to order")
    else:
        print(f"Ordeedr item {item_2} is not avaialable yet")

print(f"The total amount of itmes to pay is {order_total}")