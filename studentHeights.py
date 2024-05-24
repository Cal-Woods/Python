#Cal Woods - An app that records students height and name.

#Multiple variables that record: max height, minimum height, a counter for a later while loop, the names of the tallest and shortest students and the current height to be input.They are all created here and initialised to float, int and String values.
maxheight = float(0.0)
minheight = float(0.0)
count = int(0)
maxheightname = ""
minheightname = ""
height = float(0.0)

#an array variable as indicated by the square brackets. An array is a variable that can hold multiple values.This will keep record of student names hence the name: studentList.
studentList = []

#students is a variable which holds an int value that will be used to loop the input students amount of times.
students = int(input("Enter amount of students: "))

#A while loop that will keep going and asking for user input for name and height as long as count is less than students. count will increase each time so the loop can eventually end.
while(count < students):
    name = input("What is student's name? ")
    #Each time the loop runs the user input name will be added to studentList.
    studentList.append(name)
    
    #a variable that asks for user input in the form of a number.
    height = float(input("Enter student's height in cm. Eg. 120 = 3 ft and 9 inch.\n"))
    #An if statement that saves the first names enteres as maxheightname and minheightname.
    if(count == 0):
    	maxheight = height
    	maxheightname = name
    	minheight = height
    	minheightname = name
    
    #An if statement to check input height is within 100cm to 200cm
    if(height >= 100 and height <= 200):
    	print("This height is within the expected range of 100cm to 200cm.")
    else:
    	print("This is out of the normal range.")
    #Two if statements in the loop that check if the input height is greater than the maxheight variable or less than the minheight.
    if(height > maxheight):
        maxheight = height
        maxheightname = name

    if(height < minheight):
        minheight = height
        minheightname = name
    count = count + 1

#Once the loop has ended the rest of the code will execute. The print command will print the list of students entered and tell the user who the tallest and shortest student is.
print("Here is the list of students.",studentList,"\nThe student with the highest height was:",maxheightname,"-",studentList.index(maxheightname),"who is",maxheight,"cm.The student with the lowest height was",minheightname,"-",studentList.index(minheightname),"who is",minheight,"cm.")
#end of program.