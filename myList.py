knightsList = ["Galahad","Gawain","Arthur","Lancelot",]

print("This is an example,of a list",knightsList,"")
knightsList.append("Kay")
knightsList.append("Tristran")
knightsList.sort()
print("This is the list in alphabetical order with new names added after using the sort and append functions.",knightsList)

answer = "y"

while(answer == "y"):
	searchBar = input("Enter name to search in knightsList: ")
	
	if(searchBar == "Merlin" or searchBar == "merlin"):
		print("He is associated with Arthur and the knights but not in this list for he is not a knight.")
	
	elif(searchBar in knightsList):
		print("we found",searchBar,"in knightsList. It is number",knightsList.index(searchBar ) +1,"on the list.\n")
		
	else:
		print("That name was not found!\n")
	answer = input("Would you like to search again? 'y' or 'n'")
print("Goodbye!")