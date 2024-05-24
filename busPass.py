#Cal Woods - A program that takes a name and age so the program can determine if the input age is allowed on a bus.
name = str(input("What is your name? "))
print("Hello.", name)
print()

age = int(input("What age are you? "))

if age >= 66:
   print("Welcome to free travel on the bus.")
else:
   print("Sorry", name, "you're too young. Come back when you're 66.")
