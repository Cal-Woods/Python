#Cal Woods - A calculatoer using a while loop.
running = True

def options():
    print("Type 'a' to add two numbers\nType 's' to subtract two numbers\nType 'm' to multiply two numbers\nType 'd' to divide two numbers\nType 'q' to quit program")

def add(n1,n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2
    
def remainder(n1,n2):
	return n1 % n2
	
print("Welcome to my calculator app!\n")

while(running == True):
    options()
    answer = input("Choose: ")
    if(answer == "a"):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("The answer is",add(num1,num2))
    
    elif(answer == "s"):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("The answer is",subtract(num1,num2))
    
    elif(answer == "m"):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("The answer is",multiply(num1,num2))
    
    elif(answer == "d"):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if(num1 <=0):
        	num1 = float(input("Numbers must be above zero. re-enter numbers. Number 1:  "))
        
        if(num2 <= 0):
        	num2 = float(input("Try again!\nNumber 2:"))
        
        print("The answer is",divide(num1,num2))
    
    elif(answer == "r"):
    	num1 = float(input("Enter a number: "))
    	print(remainder(num1,num2))
    	
    elif(answer == "q"):
        running = False
    
    else:
        print("Invalid option! try again.\n")

print("Thanks for using this calculator! Bye!")
