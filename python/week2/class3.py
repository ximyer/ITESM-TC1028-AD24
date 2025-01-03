# Author: Ximena Yeraldin López López (A00842826)
# Date: Monday, August 12, 2024.

# Python program

'''
INPUT DATA:
1. Length of the hypotenuse
2. Lenght of one of the small sides (cateto 1).

OUTPUT DATA:
1.- The lenght of the missing side.


ALGORITHM:
1.- Ask the user to input the lenght of the hypotenuse, process it as a float number and save it in the variable 'hypotenuse'.
2.- Ask the user to input the lenght of the 'first' cateto, process it as a float number and save it in the variable 'cateto1'.
3.- Use the Pythagorean formula of b=√(c^2)-(a^2) to calculate the lenght of the missing cateto.
     3.1.-  Elevate to the 2nd power the hypotenuse and the cateto1.
     3.2.- Substract the 2nd power numbers.
     3.3.- Obtain the square root of the number resulting from step 3.2
     3.4.- Save the value of the result of the square root in the variable cateto2, as it is the lenght of the second side.
4.- Print the result of the square root. 



TEST CASE #1:
Please, type the lenght of the hypotenuse: 10
Now type the lenght of the first 'cateto'; 6

...

The lenght of the second 'cateto' is: 8


TEST CASE #2:
Please, type the lenght of the hypotenuse: 47
Now type the lenght of the first 'cateto'; 21

...

The lenght of the second 'cateto' is: 42.05


TEST CASE #3:
Please, type the lenght of the hypotenuse: 536
Now type the lenght of the first 'cateto'; 82

...

The lenght of the second 'cateto' is: 529.69

'''

# Python program

import math

hypotenuse = float(input("Please type the lenght of the hypotenuse: "))
cateto1 = float(input("Now, type the lenght of the first 'cateto': "))

missing_side = math.sqrt(math.pow(hypotenuse, 2) - math.pow(cateto1, 2))

print(f"The lenght of your second 'cateto' is: {missing_side:.2f}")