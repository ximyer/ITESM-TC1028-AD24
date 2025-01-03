import math

# EXERCISE 1: DRIVERS LICENSE

def exercise1(age, have_id):

     if (age >= 18 and have_id == 'yes') or (age >= 18 and have_id == 'no'):
          return "Yes"
     elif (age < 18 and have_id == 'no') or (age < 18 and have_id == 'yes'):
          return "No"
     else: 
          return "We need to check"

print(exercise1(17,'no'))


# EXERCISE 2: TRIANGLE TYPE

def exercise2(x, y, z):

     if x > 0 and y > 0 and z > 0  and x + y > z and x + z > y and y + z > x:
          if x == y and y == z:
               return "EQUILATERAL"
          elif x == y or x == z or y == z:
               return "ISOSCELES"
          else:
               return "SCALENE"
     else:
          print("Not a triangle")

print(exercise2(5,5,5))


# EXERCISE 3: GREATER THAN 3

def exercise3(a, b, c):

     if a > b and a > c:
          return f"The greatest number is: ", a
     elif b > a and b > c:
          return "The greatest number is: ", b
     elif c > a and c > b:
          return f"The greatest number is: ", c
     else:
          return "Idk wym"

print(*exercise3(755, 13, 21))

# EXERCISE 4: # ORDERING 3 NUMBERS **********

def exercise4():
     num1 = int(input("Number 1: "))
     num2 = int(input("Number 2: "))
     num3 = int(input("Number 3 : "))

     if num1 <= num2 and num1 <= num3:
          return num1
          if num2 <= num3:
               return num2
               return num3
          else: 
               return num3
               return num2
     elif num2 <= num1 and num2 <= num3:
          return num2
          if num1 <= num3:
               return num1
               return num3
          else: 
               return num3
               return num1
     elif num3 <= num1 and num3 <= num3:
          return num3
          if num1 <= num2:
               return num1
               return num2
          else: 
               return num2
               return num1
          return "No valid data"


# EXERCISE 5: BODY MASS INDEX 

def exercise5(weight, height):

     index = weight / height**2

     if index < 20:
          return "LOW WEIGHT"
     elif 20 <= index < 25:
          return "NORMAL"
     elif 25 <= index < 30:
          return "OVERWEIGHT"
     elif 30 <= index < 40:
          return "OBESITY"
     elif index >= 40:
          return "MORBID OBESITY"
     else:
          return "No valid data"

decision5 = exercise5(66, 1.64)
print(decision5)

# EXERCISE 6: LEAP-YEAR

def exercise6(year):

     if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
          return True
     else: 
          return False

print(exercise6(2005))


# EXERCISE 7: NEXT DAY

def exercise7():

     year = int(input("Year: "))
     month = int(input("Month: "))
     day = int(input("Day: "))


     if month in [1, 3, 5, 7, 8, 10]:
          if day == 31:
               print(year)
               print(month + 1)
               print("1")
          else:
               print(year)
               print(month)
               print(day + 1)
     elif month in [ 4, 6 ,9, 11]:
          if day == 30:
               print(year)
               print(month + 1)
               print("1") 
          else:
               print(year)
               print(month)
               print(day + 1)
     elif month == 2 and day == 28:
          if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
               print(year)
               print(month)
               print(day + 1)
          else:
               print(year)
               print(month + 1 )
               print("1")
     elif month == 12 and day == 31:
          print(year + 1)
          print("1")
          print("1")
     else:
          print("There's no date")


# EXERCISE 8: POSITION OF A POINT WITH RESPECT TO THE CIRCUMFERENCE

def exercise8(radius, x1, x2, y1, y2):

     distance = math.sqrt(((x2 - x1)**2) + ((y2 - y1)**2))

     if distance < radius:
          return "INSIDE"
     elif distance == radius:
          return "ON"
     else:
          return "OUTSIDE"

print(exercise8( 7, 0, 0, 1, 9))

# EXERCISE 9: FROM CM TO KM, M AND CM

def exercise9(distance):

     km = distance // 100000
     m = (distance % 100000) // 100
     cm = distance % 100

     if km > 0:
          print(f"{km} km")
     if m > 0:
          print(f"{m} m")
     if cm > 0:
          print(f"{cm} cm")

print(exercise9(300004))


# EXERCISE 10: COMPARE DATES

def exercise10():
     day1 = int(input("Day 1: "))
     month1 = int(input("Month 1: "))
     day2 = int(input("Day 2: "))
     month2 = int(input("Month 2: "))

     print("---------- ")

     if month1 < month2:
          print("Date 1 occurs first.")
     elif month2 < month1:
          print("Date 2 occurs first")
     elif month1 == month2:
          if day1 < day2:
               print("Date 1 occurs first")
          elif day1 == day2:
               print("It's the same date")
          else:
               print("Date 2 occurs fist")
     else:
          print("Wrong data")


# EXERCISE 11: QUADRANTS

def exercise11():
     
     integer = int(input("Degrees: "))

     if integer == 0 or integer == 90 or integer == 180 or integer == 270 or integer == 360:
          print("Axis")
     elif 1 <= integer <= 89:
          print("Quadrant 1")
     elif 91 <= integer <= 179:
          print("Quadrant 2")
     elif 181 <= integer <= 269:
          print("Quadrant 3")
     elif 271 <= integer <= 359:
          print("Quadrant 4")
     elif integer < 0:
          print("Exceeds")
     else:
          print("Invalid data")


# EXERCISE 12: QUADRATIC FUNCTIONS

def exercise12():

     a = int(input("a: "))
     b = int(input("b: "))
     c = int(input("c: "))

     if a == 0 and b == 0:
          print("No Solution")
     elif a == 0 and b != 0:
          x = -c / b
          print(x)
     elif a != 0:
          discriminant = (b ** 2) - (4 * a * c)
          if discriminant < 0:
               print("Complex Roots")
          elif discriminant > 0:
               x1 = (-b + math.sqrt (discriminant))/ (2*a)
               x2 = (-b - (math.sqrt(discriminant)) / (2*a))
               print(x1)
               print(x2)
          else:  #discriminant == 0
               x = -b / (2 * a)
               print(x)
     else:
          print("Data error")


# EXERCISE 13: MINI GAME, ROCK, PAPER, SCISSORS:

def exercise13():
     ana = input("Your game, Ana? ")
     juan = input("Your game, Juan? ")

     if (ana == "a" and juan == "a") or (ana == "p" and juan == "p") or (ana == "t" and juan =="t"):
          print("Tie")
     elif (ana == "a" and juan == "t") or (ana == "t" and juan == "p") or (ana == "p" and juan == "a"):
          print("Ana Wins!")
     elif (juan == "a" and ana == "t") or (juan == "t" and ana == "p") or (juan == "p" and ana == "a"):
          print("Juan Wins!")
     else:
          print("Not valid rolls")


# INTERACTIVE MENU FOR THE USER

print("My Homework 3 Menu:")
print("1) Driver License")
print("2) Triangle Type")
print("3) Greater than 3")
print("4) Order 3 numbers")
print("6) Leap-year")
print("7) Next day")
print("8) Position of a point with respect to the circumference")
print("9) From Cm to Km, M and Cm")
print("10) Compare Dates")
print("11) Quadrant")
print("12) Quadratic")
print("13) Mini game Rock, Paper, Scissors")
print("--------------")

choice = int(input("Enter your choice: "))
print("--------------")

exercises = {
     1: exercise1,
     2: exercise2,
     3: exercise3,
     4: exercise4,
     5: exercise5,
     6: exercise6,
     7: exercise7,
     8: exercise8,
     9: exercise9,
     10: exercise10,
     11: exercise11,
     12: exercise12,
     13: exercise13,
}

if choice in exercises:
     exercises[choice]()
else:
     print("I don't have so many exercises, lol")