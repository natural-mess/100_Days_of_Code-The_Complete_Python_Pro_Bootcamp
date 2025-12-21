print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

# print(f"Each person should pay: ${((bill/people)*(1+(tip/100))):.2f}")

print(f"Each person should pay: ${"{:.2f}".format(((bill / people) * (1 + (tip / 100))))}")
