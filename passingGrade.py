#Cal Woods - A program that determines what grade you got based on QQI standards.

total = int(input("What was your percentage on the module? "))

if(total >= 80):
    print("You got a distinction!")

elif(total >= 65):
    print("You got a merit!")

elif(total >= 50):
    print("You got a pass.")

else:
    print("You did not pass.")
print("End of program.")
