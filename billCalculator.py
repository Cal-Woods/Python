#Cal Woods - An app for paying a bill with a tip

bill = float(input("How much is the bill?"))
tip = float(input("How much are you tipping? Please enter percentage in decimal format:"))
bill = round(bill, 2)
tip = round(tip, 2)
people = int(input("How many people are splitting the bill?"))

print("The total bill comes to",round((bill + bill * tip)  / people,2),"Euro each.")