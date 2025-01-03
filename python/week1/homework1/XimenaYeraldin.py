#User's inputs
item_price = int(input("What's the price of this item?: $"))
number_of_items = int(input("How many items are you buying?: "))

#Calculations
real_price = item_price * number_of_items
tax = real_price * 0.16
final_price = real_price + tax

#Discount


#Print the details
print("Items: ", number_of_items)
print("Price per item: $", item_price)
print("Tax: $", tax)
print("The final price of this items is: $", (final_price))