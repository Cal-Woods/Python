#Cal Woods - Another program that gives multiple options using 'def' command.
loop = True

def options():
    print("Press 'l' to see litres to pints.\nPress 'p' to see pints to litres.\nPress 'o' to see options again.\n Press 'q' to quit.\n")


def pints_to_litres(pints):
    return round(pints / 2.113,2)

def litres_to_pints(litres):
    return round(litres * 2.113,2)

while loop == True:
    options()
    answer = input("Choose an option: ")
    
    if(answer == "o"):
        options()
    
    elif(answer == "p"):
        pint = float(input("Enter pints to convert to litres: "))
        print(pints_to_litres(pint))

    elif(answer == "l"):
        litre = float(input("Enter litres to convert to pints: "))
        print(litres_to_pints(litre))

    elif(answer == "q"):
        loop = False

    else:
        print("That is not a valid option! Try again.")
        options()

print("Thanks for using this program! Goodbye!")
