#Cal Woods - A program to add numbers as many times as you want.

repeat = "y"

while repeat == "y":
    firstnumber = int(input("Enter first number to add: "))
    secondnumber = float(input("Enter second number to add: "))
    sumofnumbers = firstnumber + secondnumber
    print("The answer is",sumofnumbers,".")
    repeat = input("Would you like to go again? Y/N ")
    repeat = repeat.lower()
    
print("Thanks. Have a beautiful time!")