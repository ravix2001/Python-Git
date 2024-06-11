import os

# Clearing the Screen
os.system('cls')

menu = {
    'pizza': 400,
    'burger': 80,
    'momo': 100,
    'chowmin': 100,
    'coffee': 80,
    'tea': 20
}

def show_menu():
    print("1. Pizza --- Rs.400\n2. Burger --- Rs.80\n3. MoMo --- Rs.100\n4. Chowmin --- Rs.100\n5. Coffee --- Rs.80\n6. Tea --- Rs.20")

def order():
    order_total = 0
    more_item = True
    while more_item == True:
        items = input("Please enter the item you want to order : ").lower()
        if items in menu:    
            ordered_items = items
            print(ordered_items)
            order_total += menu[items]
            print(order_total)
        else:
            print("Sorry, this item is not available in our cafe")
        more_item = input("Do you want to add more ?[y/n] : ").lower()
        if(more_item == 'y'):
            more_item = True
        else:
            more_item = False
    print(f"Total Bill Amount : Rs.{order_total}\nThank you!")

print("-------------    Welcome to Python Cafe    -------------")
show_menu()
order()
