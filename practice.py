#Cal Woods - A program that converts dollars to other currencies.

#Creating variables for saving user input.
userinput = str()
#Storing different currency conversion rates from US dollars in a list
rates = [0.95136, 0.84286, 134.29, 1.3619]

#printing app menu using a function
def menu():
	return "1) Convert US Dollars to Euro\n2) Convert US Dollars to Japanese Yen\n3) Convert US Dollars to Pound Sterling\n4) Convert US Dollars to Turkish Lira"

print(menu())

userinput = str(input("Please choose menu option by typing the corresponding number?"))

loop = True

while(loop == True):
	dollars = float(input("Please enter a Dollar amount? Numbers only!"))

	if(userinput == "0"):
		loop = False
	
	elif(userinput == "1"):
		print(dollars, "US Dollars is equal to",dollars * rates[0], "Euro.")
		userinput = str(input("Please choose menu option by typing the corresponding number?"))
		
	elif(userinput == "2"):
		print(dollars, "US Dollars is equal to",dollars * rates[2], "Japanese Yen.")
		userinput = str(input("Please choose menu option by typing the corresponding number?"))

	elif(userinput == "3"):
		print(dollars, "US Dollars is equal to",dollars * rates[1], "Pound Sterling.")
		userinput = str(input("Please choose menu option by typing the corresponding number?"))
		
	elif(userinput == "4"):
		print(dollars, "US Dollars is equal to",dollars * rates[3], "Turkish Lira.")

	userinput = str(input("Please choose menu option by typing the corresponding number?"))		
	print("\n\n",menu())