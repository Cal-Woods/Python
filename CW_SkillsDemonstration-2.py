#Cal Woods CSN B - A program to perform Conversions using functions. Skills demonstration 2.

#The text of the program menu which is printed within a function called Menu.
def Menu():
	print("\n\n\nPlease type the corresponding number to select an option from the available menu options:\n(1	Miles to Kilometres\n(2	Kilometres to Miles\n(3	Celsius to Fahrenheit\n(4	Fahrenheit to Celsius\n(5	Pints to Litres\n(6	Litres to Pints\n(7	Kg to Stone\n(8	Stone to Kg\n(9	Acres to Hectares\n(10	Hectares to Acres")


#A function that performs a miles to kilometres conversion.
def milesToKilometres():
	miles = float(input("Please enter a distance value in miles: "))
	rate = float(1.609344)
	convert = float(round(miles * rate, 2))
	return convert

#A function that performs a kilometres to miles conversion.
def kilometresToMiles():
	km = float(input("Please enter a distance value in kilometres: "))
	rate = float(1.609344)
	convert = float(round(km / rate, 2))
	return convert


#A function that performs a Celsius to Fahrenheit conversion.
def celsiusToFahrenheit():
	celsius = float(input("Please enter a temperature value in degrees Celsius: "))
	convert = float(round((celsius*(9/5)) + 32, 2))
	return convert

#A function that performs a Fahrenheit to Celsius conversion.
def fahrenheitToCelsius():
	fahrenheit = float(input("Please enter a temperature value in degrees Fahrenheit: "))
	convert = float(round((fahrenheit-32) * (5/9), 2))
	return convert

#A function that performs a Pints to Litres conversion.
def pintsToLitres():
	pints = float(input("Please enter a volume value in Imperial Pints: "))
	rate = float(1.76)
	convert = float(round(pints / rate, 2))
	return convert

#A function that performs a Litres to Pints conversion.
def litresToPints():
	litres = float(input("Please enter a volume value in litres: "))
	rate = float(1.76)
	convert = float(round(litres * rate, 2))
	return convert

#A function that performs a Kg to Stone conversion.
def kgToStone():
	kilograms = float(input("Please enter a mass value in kg: "))
	rate = float(6.35)
	convert = float(round(kilograms / rate, 2))
	return convert

#A function that performs a Stone to Kg conversion.
def stoneToKg():
	stone = float(input("Please enter a mass value in stone: "))
	rate = float(6.35)
	convert = float(round(stone * rate, 2))
	return convert

#A function that performs an Acre to Hectare conversion.
def acresToHectares():
	acres = float(input("Please enter an area value in acres: "))
	rate = float(2.471)
	convert = float(round(acres / rate, 2))
	return convert

#A function that performs a Hectare to Acre conversion.
def hectaresToAcres():
	hectares = float(input("Please enter an area value in hectares: "))
	rate = float(2.471)
	convert = float(round(hectares * rate, 2))
	return convert


#Using a while loop, I will implement the user's choices for the app menu using if statements and the Menu function to display the app menu.

#A variable called another that is set to the char value of y.
another = 'y'

#A while loop that will keep running, as long as the variable "another" is set to the character, 'y'.
while(another == 'y'):
	
	#Calling the Menu() function, which displays all of the menu options.
	Menu()
	
	#A variable called choice that asks for user input, formatted as a String. This is so the user can navigate the menu with the specified inputs.
	choice = str(input("Choose a menu option: "))
	
	if(choice == "1"):
		print(milesToKilometres())
	
	elif(choice == "2"):
		print(kilometresToMiles())
		
	elif(choice == "3"):
		print(celsiusToFahrenheit())
		
	elif(choice == "4"):
		print(fahrenheitToCelsius())
		
	elif(choice == "5"):
		print(pintsToLitres())
		
	elif(choice == "6"):
		print(litresToPints())
		
	elif(choice == "7"):
		print(kgToStone())
		
	elif(choice == "8"):
		print(stoneToKg())
		
	elif(choice == "9"):
		print(acresToHectares())
		
	elif(choice == "10"):
		print(hectaresToAcres())
	
	#An elif statement that checks if the q character has been entered. if this is true, the app will finish by changing the variable "another", exiting the loop.
	elif(choice == 'q'):
		another = 'N'
		print("Goodbye!")
	
	#An else statement that is executed if the if and elif statements are all false
	else:
		print("Invalid Option! Please try again.")