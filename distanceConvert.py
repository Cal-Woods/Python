#Cal Woods - A program that gives multiple options using 'def' command.
loop = True

def options():
    print("Type 'm' to see miles to kilometres.\nType 'k'' to see kilometres to miles.\nType 'p' to see options again.\nType 'q' to quit")


def kilometres_to_miles(kilometres):
    return round(kilometres / 1.609,2)

def miles_to_kilometres(miles):
    return round(miles * 1.609,2)

options()
while loop == True:
    answer = input("Choose an option: ")
    
    if(answer == "p"):
        options()

    elif(answer == "m"):
        mile = float(input("Enter miles to convert to kilometres: "))
        print(miles_to_kilometres(mile),"\n")
        
    elif(answer == "k"):
        kilo = float(input("Enter kilometres to convert to miles: "))
        print(kilometres_to_miles(kilo),"\n")

    elif(answer == "q"):
        loop = False

    else:
        print("That is not a valid option! Try again.")
    
print("Thanks for using this app. Bye!")