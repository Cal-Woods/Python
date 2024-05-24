#Cal Woods - An app that records students weight and name.

students = []
maxweight = float(0.0)
minweight = float(45.0)
count = int(1)
maxweightname = ""
minweightname = ""
studentnum = int(input("Enter amount of students: "))
while(count <= studentnum):
    name = input("What is student's name? ")
    weight = float(input("Enter student's weight in Kg: "))
    students.append(name)

    if(weight > maxweight):
        maxweight = weight
        maxweightname = name

    if(weight < minweight):
        minweight = weight
        minweightname = name
    
    count = count + 1
    
print("The students are: ",students,".")
print("The student with the highest weight was:",maxweightname,"-",students.index(maxweightname),"weighing",maxweight, "lbs.")

if(minweight != 45.0):
	print("The student with the lowest weight was:",minweightname,"-",students.index(minweightname),"weighing",minweight, "lbs.")