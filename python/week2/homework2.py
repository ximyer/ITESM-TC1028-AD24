'''
Student: Ximena Yeraldin López López (A00842826)
Date: Wednesday, August 14, 2024.
'''

import math

# 💡 Inicializar la lista fuera del bucle
list_interests = []

for i in range (5):
     print(f"CLIENT {i + 1} ")
     principal_amount = float(input("Please give me the principal amount of money you want to save: "))
     annual_rate_interest = float(input("Now, please give me the annual rate of interest the bak offered you (%): "))
     time_period = int(input("Lastly, how many years you intend to save your money in here? "))

     simple_interest = (principal_amount * annual_rate_interest * time_period) / 100

     print("Your simple interest amount is: ", simple_interest)
     print ("----------")

     # 💡 Agregar el resultado a la lista 
     list_interests.append(simple_interest)

print("Which is the lowest simple interest? ", min(list_interests))
print("Which is the highest simple interest? ", max(list_interests))
print("Display the 5 simple interests calculated: ", list_interests)
print("What is the average of the simple interests? ", sum(list_interests)/len(list_interests))