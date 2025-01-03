#User's inputs - Shopping Cart 
item_name = input("What's the name of this item?: ")
item_price = float(input("What's the price of this item?: $"))
number_of_items = 5
subtotal = item_price * number_of_items

#Special Discount
discount_ticket = float(input("If you have a discount ticket, please input your discount so I can calculate your new price: "))
discount_price = subtotal - discount_ticket

#Taxes
tax = discount_price * 0.16

#Pay
final_price = discount_price + tax

#Print the details
print("Subtotal: ", subtotal)
print("Discount: ", discount_ticket)
print("Tax / IVA (16%): $", tax)
print("The final price of this items is: $", (final_price))

