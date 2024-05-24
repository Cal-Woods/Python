#Cal Woods - Loud Nightclub. This program checks the user's age to determine whether or not they are allowed in to a nightclub.

name = input("What is your name?")
age = int(input("What is your age?"))

if(age >= 18):
    print("Welcome to the nightclub",name,"is it?")

else:
    print("Sorry",name,"not tonight!")

print("Bye!")
