#Cal Woods - A program that allows the user to enter numbers in a while loop and get the sum and average
print("Getting the sum and average of a set of numbers.\n")

number = 1
nsum = 0
count = 0

while(number != 0):
    number = int(input("Enter number: "))
    nsum = float(nsum + number)
    count = count + 1
	
average = nsum / (count - 1)
print("The sum of the calculation is",nsum,"and the average of the calculation is",average,".")        
