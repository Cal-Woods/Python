#Cal Woods - Converting celsius to fahrenheit and back again.
answer = "y"

print("Welcome to degrees fahrenheit to celsius program!")

while(answer != "n"):
	fahrenheit = float(input("Enter degrees fahrenheit amount to convert to celsius? "))

	celsius = float(round((fahrenheit - 32.0) * 5.0 / 9.0,2))

	print("\n",fahrenheit,"fahrenheit converted to degrees celsius is",celsius,"degrees celsius. \n")

	celsius = float(input("Enter degrees celsius amount to convert to fahrenheit? "))
	fahrenheit = float(round((9.0 / 5.0) * 		celsius + 32.0,2))
	print("Whereas",celsius,"degrees celsius is equal to",fahrenheit,"degrees fahrenheit.\n\n")
	answer = input("Do you want to do that again? Type 'y' or 'n'")
print("Thank you for using this program.")