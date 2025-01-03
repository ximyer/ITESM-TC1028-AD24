'''
As of friday august 09, 2024 at 23:23
Student: Ximena Yeraldin López López (A00842826)
'''


#User's inputs - Shopping Cart 

for i in range (5):
     print(f"Item #", {i+1})
     item_name = input("What's the name of this item?: ")
     item_price = float(input("What's the price of this item?: $"))
     item_number = int(input("How many items are you buying? "))

shopping_cart = {item_name, item_price, item_number}

for i in range (5): 
     individual_prices = shopping_cart[item_price] * shopping_cart[item_number]

subtotal = {individual_prices}
subtotal_in_numbers = subtotal(int)

#Special Discount
discount_ticket = float(input("If you have a discount ticket, please input your discount so I can calculate your new price: "))
discount_price = subtotal_in_numbers - discount_ticket

#Taxes
tax = discount_price * 0.16

#Pay
final_price = discount_price + tax

#Print the details
print("Subtotal:", subtotal)
print("Discount: ", discount_ticket)
print("Tax out of (16%): $", tax)
print("The final price of this items is: $", (final_price))
