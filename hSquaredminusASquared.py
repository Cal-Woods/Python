import math

print("Please enter the lengths of the longest side and the known shorter side of the triangle? Remember, Side h has to be the biggest.")

a = float(input("Side a:"))
h = float(input("Side h:"))
while(h < a):
	h = float(input("Make sure that h is bigger or the same as a. Reenter h:"))

print("Side O of the triangle is",round(math.sqrt((h ** 2) - (a ** 2)),2),".")