grades = []

for i in range (5):
     grade = int(input("Give me a grade: "))
     grades.append(grade)

average = sum(grades) /len(grades)
print(average)



'''
brands = ["Amazon", "Tesla", "Meta", "Google"]
user_idea = input("Give me an idea / a brand: ")
brands.append(user_idea)
print(brands)


brands = ["Amazon", "Tesla", "Meta", "Google"]

user_input = input("Give me a brand: ")
exists = False

for brand in brands:
     if user_input == brand:
          exists = True

if exists:
     print("It exists!")
else:
     print("Doesn't exist :(")



numbers = [23, 45, 67,12, 67, 23, 45, 56]

total_sum = 0

for number in numbers: 
     total_sum += number

average = total_sum / len(numbers)
print(average)
'''