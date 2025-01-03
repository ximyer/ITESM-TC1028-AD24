def exercise7(year, month, day):

     if month in [1, 3, 5, 7, 8, 10]:
          if day == 31:
               return year
               return month + 1
               return 1
          else:
               return year
               return month
               return day +1
     elif month in [ 4, 6 ,9, 11]:
          if day == 30:
               return year
               return month + 1
               return 1
          else:
               return year
               return month
               return day + 1
     elif month == 2 and day == 28:
          if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
               return year
               return month
               return day + 1
          else:
               return year
               return month + 1
               return 1
     elif month == 12 and day == 31:
          return year + 1
          return 1
          return 1
     else:
          return "There's no date"

decision7  = exercise7(2020, 12, 22)
print(decision7)