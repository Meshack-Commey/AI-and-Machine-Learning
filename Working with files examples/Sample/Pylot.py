#Pylottery

import random

#Initialise an empty list that will be used to store the 5 lucky numbers

lotteryNumbers = [ ]
for i in range(0, 5):
	number = random.randint(1, 90)
    #Check if this number has already been picked and .........
	while number in lotteryNumbers:
		#.... if it has, pick a new number instead
		number = random.randint(1, 90)
		#Now that we have a unique number, lets append it to our list.
	lotteryNumbers.append(number)
#Sort the list in ascending order
lotteryNumbers.sort()

#Initialise an empty list that will be used to store User Ticket Numbers

userNumbers = [ ]
for i in range(0, 5):
	number = int(input("Please enter a number between 1 and 90 inclusive : "))
	while (number in userNumbers or number < 1 or number > 90):
		print("Invalid number, please try again : ")
		number = int(input("Please enter a number between 1 and 90 inclusive: "))
	userNumbers.append(number)

#Display the list on screen
print(">>> Today's lottery numbers are : ")
print(lotteryNumbers)
print(" ")
print(">>> Your selection : ")
print(userNumbers)
print(" ")
counter = 0
for number in userNumbers:
	if number in lotteryNumbers:
		counter +=1
print("You guessed " + str(counter) + " numbers correctly.")