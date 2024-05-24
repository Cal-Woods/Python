#A program that does pythagoras theorem using the two shorter sides of a triangle.

import math

print("Please enter the lengths of the two shorter sides of the triangle?")

a = float(input("Side a:"))
o = float(input("Side o:"))

print("The longest side, or the hypotenuse, of the triangle is",round(math.sqrt((a ** 2) + (o ** 2)),2),"centimetres squared.")