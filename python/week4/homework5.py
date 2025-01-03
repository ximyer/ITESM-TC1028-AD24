import math

# CYLINDER AREA AND VOLUME

def cylinder_area(radius, height):
     return 2 * math.pi * radius * (height + radius)

def cylinder_volume(radius, height):
     return math.pi * (radius ** 2) * height

print(cylinder_area(5, 7))
print(cylinder_volume(5,7))


#CONVERT TO CM

def feet_to_cm(feet):
     return feet * 30.48

def inches_to_cm(inches):
     return inches * 2.54

def yards_to_cm(yards):
     return yards * 91.44

print(feet_to_cm(10))
print(inches_to_cm(10))
print(yards_to_cm(10))

# CALCULATE GRADE

def calculate_grade(score):
     
     if score >= 1.0:
          return "Incorrect Input"
     elif score > 0.9:
          return "A"
     elif score > 0.8:
          return "B"
     elif score > 0.7:
          return "C"
     elif score > 0.6:
          return "D"
     elif score <= 0.6:
          return "F"
     else:
          return "Wrong data"
     
print(calculate_grade(0.5))


# LEAP YEAR

def leap_year(year):

     if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
          return True
     else: 
          return False

print(leap_year(2005))


# MENU

print("My Homework 5 Menu:")
print("1) Convert to CM")
print("2) Cylinder and Area")
print("3) Calculate Grade")
print("4) Leap Year")
print("5) Finish Program")
print("--------------")

choice = int(input("Enter your choice: "))
print("--------------")


if choice == 1:
     feet_to_cm()
     inches_to_cm
     yards_to_cm
elif choice == 2:
     cylinder_area()
     cylinder_volume()
elif choice == 3:
     calculate_grade()
elif choice == 4:
     leap_year()
else:
     print("Finished")