
'''
# PRINT THE MENU DISPLAY FOR THE USER TO CHOOSE WHICH OPTION THEY WANT
print("MENU DISPLAY")
print("1. Display all products")
print("2. Add product to stock")
print("3. Add stock to a product")
print("4. Remove stock from a product")
print("5.Check stock levels")
print("6. Exit")
print("--------------")

choice = int(input("Enter your choice: "))
print("--------------")

choices = {
     1: display_products(),
     2: add_product(),
     3: add_stock(),
     4: remove_stock,
     5: check_stock,
     6: is_done,
} 

if choice in choices:
     choices[choice]()
else:
     print("I don't have so many exercises, lol")
'''

# CREATE A LIST WITH PRODUCTS


products = {product, quantity, item_treshold}


# DISPLAY ITEMS

def display_items(item, quantity, item_treshold):
     return products

# ADD ITEM
     product = input("Name of the product: ")
     quantity = int(input("Quantity: "))
     item_treshold = input("Treshold: ")
