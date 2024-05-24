import math

def Menu():
	print("Welcome to a maths game! In this game you will try to solve math questions that will increase in difficulty\n\n (1) Play\n (2) Exit")
	c = int(input(": "))
	if(c == 1):
		Play()
	elif(c == 2):
		print("See you next time!")
		return
	else:
		print("Invalid choice, Try again!")
		Menu()
		
		
def Play():
	score = int(0)
	
	print("A triangle has three sides called a, o, h. a is 14 cm, o is 06 cm, find h, rounding down to the nearest whole number?")
	
	a1 = float(input("Answer: "))
	
	if(a1 == round(math.sqrt((14 ** 2)  + (6 ** 2)),2)):
		 print("Correct! You gain a point.")
		 score = score + 1
		 print(score,"out of 3")
	else:
		print("Incorrect! Next Question.")
	
	print("\nFind the mean of this list of numbers.\n4, 3, 8, 8, 8, 6, 5, 4, 7, 7")
	
	a2 = float(input("Answer: "))
	
	if(a2 == round((4 + 3 + 8 + 8 + 8 + 6 + 5 + 4 + 7 + 7) / 10,2)):
		print("Correct! You gain a point!")
		score = score + 1
		print("\nYou now have",score,"out of 3.")
	else:
		print("Incorrect! Your score is",score,"out of 3. Next Question!")
	
	print("\nFinal Question!\nThe exchange rate of euro to yen is 1 euro is 138.92 japanese yen. find out how much €500 is in yen.")
	a3 = float(input("Answer: "))
	
	if(a3 == round(500 * 138.92,2)):
			score = score + 1
			print("\nCorrect! You now have",score,"out of 3.")
	else:
		print("Incorrect! Your score is",score,"out of 3. Next Question!")

	if(score == 3):
		print("Congratulations! You got all of them right!\n\n")
		Menu()
	elif(score == 2):
		print("Well done. You scored",score,"out of 3 questions. That's pretty good but you can do better.")
		print()
		print()
		Menu()
	else:
		print("You scored",score,"out of 3. This is too low. Try again:")
		print()
		print()
		Menu()

print("Math game \n".upper())
Menu()