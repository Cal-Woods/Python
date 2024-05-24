# converts distances between miles and kilometres

def print_options():
    print("Options:")
    print(" 'p' print options")
    print(" 'm' convert from miles")
    print(" 'k' convert from kilometres")
    print(" 'q' quit the program")
 
def miles_to_kilometres(miles):
    return miles*1.6
 
def kilometres_to_miles(kilometres):
    return kilometres*0.6
 

choice = "p"  # Setting choice to p.

while choice != "q":

    if choice == "m":
        miles = float(input("Please enter distance in miles: "))
        print(miles,"miles is equal to", miles_to_kilometres(miles),"kilometres.")
        print()
        choice = input("Please choose an option from the menu:")

    elif choice == "k":
        kilometres = float(input("Please enter distance in kilometres: "))
        print(kilometres,"kilometres is equal to",kilometres_to_miles(kilometres), "miles.")
        print()
        choice = input("Please choose an option from the menu: ")

    elif choice == "p":  
        print_options()
        print()
        choice = input("Please choose an option from the menu: ")
        print()
print()
print("Program run ended. Thank you for using convert2.py.")


















