'''
input1 = float(input("Please give me a number: "))
input2 = float(input("Please give me a number: "))
input3 = float(input("Please give me a number: "))
input4 = float(input("Please give me a number: "))
input5 = float(input("Please give me a number: "))

numbers = [input1, input2, input3, input4, input5]

print(max(numbers))
print(min(numbers))
print(sorted(numbers))
'''

numbers = []
for i in range(5):
     number = int(input("Please give me a number: "))
     numbers.append(number)
     i = i+1

print(max(numbers))
print(min(numbers))
print(slice(numbers))
print(sorted(numbers))
