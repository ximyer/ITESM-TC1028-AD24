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