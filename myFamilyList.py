#Cal Woods - A list of my family members.
myFamily = ["Rhys","Casey","Izzie","Shane","Nadine"]
print("",myFamily,"This is a list of my family members.")
count = int(0)
amount = int(input("Enter a number of new entries to add: "))

while count < amount:
	member = str(input("Enter name to add: "))
	myFamily.append(member)
	count = count + 1
	
print("\nThis is the same list after using the append function to add entries.",myFamily,"\nHere is the list in alphabetical order.\n")
myFamily.sort()
print("",myFamily,"As you can see, my brother Rhys is number",myFamily.index("Rhys") + 1,"on the list and my mother Nadine is number",myFamily.index("Nadine") + 1,"on the list.\nNow I am going to search for a specific name in my list using the in keyword in an if statement.")

another = "y"
while another != "n":
    searchBar = input("Enter a name to search in myFamily list: ")
    if(searchBar in myFamily):
        print("Found",searchBar,"\nIt is number",myFamily.index(searchBar)+ 1,"in myFamily list.")

    else:
        print("Sorry! We could not find the name",searchBar,"in myFamily list.")
    another = input("Wanna search again? 'y' or 'n'")
print("[End of program!]")