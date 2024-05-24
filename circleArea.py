#Cal Woods - Calculating the area of a circle
pie = float(3.14159)

r = float(input("Please enter radius value of circle: "))
area = float(round(pie*(r ** 2),2))
perimeter = 2 * pie * r
print("The area of this circle is",area,"metres squared. The perimeter is",perimeter,"metres.")