# HOMEWORK 3.1

def homework1():

     weight = float(input("Weight in kg: "))
     height = float(input("Height in m: "))

     bmi = weight / height**2

     if bmi < 18.5:
          print("Underweight")
     elif 18.5 <= bmi < 24.9:
          print("Normal Weight")
     elif 25 <= bmi < 29.9:
          print("Overweight")
     elif bmi >= 30:
          print("Obesity")
     else:
          print("No valid data")


# HOMEWORK 3.2

def homework2():

     grades = []

     for i in range (6):
          print(f"GRADE {i+1}")
          individual_grade = float(input("Input your grade:" ))

          grades.append(individual_grade)

     average = sum(grades)/len(grades)

     if 90 <= average <= 100:
          print(average, "A")
     elif 80 <= average <= 89:
          print(average, "B")
     elif 70 <= average <= 79:
          print("C")
     elif 60 <= average <= 69:
          print(average, "D")
     elif average <= 60:
          print(average, "F")
     else:
          print("Wrong data")


print("My Homework 3 Menu")
print("1) BMI Calculator")
print("2) Grades Average Calculator")
print("-----------")

choice = int(input("What you wanna test? "))

print("-----------")

if choice == 1:
     homework1()
elif choice == 2: 
     homework2()
else:
     print("No valid data")