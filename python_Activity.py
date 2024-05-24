#Cal Woods - A program for this week's homework.

loop = 'y'
#A function detailing a user interface application called menu().
def menu():
    print("Press 1 for Program One, 2 for Program two and 3 for Program three.\n")
    print("1 Program one\n")
    print("2 Program two\n")
    print("3 Program Three\n")

	#A function defining the first program
def first_program():
    print(int(15))
    print(str("fifteen"))

#A function for the second part of the program.
def second_program():
    name = str(input("What is your name?"))
    age = int(input("What is your birth year?"))
    year = int(2023)
    print("Nice to meet you",name, "I see you are",year - age,"years old.")
    
#A function describing instructions for the third program.
def third_program():
    weight = float(input("What is your weight in lbs?"))
    weightinkg = float(round(weight * 0.45359237, 2))	
    print("Your weight is",weight,"lbs. Converted, this equals",weightinkg,"kg.")

while loop == 'y':
    option = str("0")
    menu()
    option = str(input("Please choose an option? "))
    
    if(option == "1"):
       first_program()
       
    elif(option == "2"):
        second_program()

    elif(option == "3"):
        third_program()

    else:
        print("That is not a valid option!")

    end_program = str(input("Do you want to quit? 'Y', 'N'"))
    ans = end_program.upper()
    if(ans == 'Y'):
       loop = 'n'
    elif(ans != 'Y'):
        print("Let's go again!")
