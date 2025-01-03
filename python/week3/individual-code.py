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