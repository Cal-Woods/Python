#Cal Woods - Example of Python elif statement.

total = int(input("What are your total marks? "))

while(total > 600):
   total = int(input("That is too much! Try again. \nWhat are your total marks? "))
   
if(total >= 540):
    print("Congratulations! \nYou are eligible for a full scholarship!")

elif(total >= 480):
    print("Congratulations!\nYou are eligible for a 50 percent scholarship!")

elif(total >= 400):
    print("You are eligible for a 10 percent scholarship!")

else:
    print("We are sorry to inform you that you are not eligible for a scholarship at this time. Good luck next time.")
