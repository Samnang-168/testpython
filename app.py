
print("===welcome to the tip calculator===")
bill= float(input("what was the total bill ?"))
tip=float(input("how much tip you like to give? 10, 12, 15"))
people=int(input("how many people to split the bill?"))
total = (bill+((tip/100)*bill))/people
print(f'Each person should pay: {total}')