#Cal Woods-This program converts pound sterling to euro

sterling = float(input("Enter amount in pounds sterling: "))
euro = float(round(sterling/0.8949,2))
print("You have",euro,"euro available to spend.")