#If the bill was $150.00, split between 5 people, with 12% tip. 
print("welcome to the tip calculator!")

bill_total = float(input("what was the total bill?"))
tip_percent = float(input("How much tip would you like to give?")) / 100
num_people = float(input("How many people to split the bill?"))

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
each_pay = round((bill_total / num_people) * (1.0 + tip_percent), 2)
print("Each person should pay: $" + f"{each_pay}")