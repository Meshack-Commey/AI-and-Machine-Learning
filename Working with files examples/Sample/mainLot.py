import random, time

### TODO = Refactor GetDrawNumbers (add timers)
### TODO = Refactor CheckNumbers

#Draw Generator
def GetDrawNumbers():
	drawNumbers = [ ]
	for i in range(5):
		x = None
		while (x == None or x in drawNumbers):
			x = random.randint(1, 91)
		drawNumbers.append(x)
	return drawNumbers

#Checking my ticket with the Draws
def CheckNumbers(myTicket, actualNumbers):
	numbersMatched = 0
	for number in myTicket:
		if number in actualNumbers:
			numbersMatched += 1
	return numbersMatched
	
def DrawMatchedNumbers(myTicket, actualNumbers):
	for number in myTicket:
		if number in actualNumbers:
			while True:
				print(number)
	
### Script starts here

startTime = time.perf_counter()

myNumbers = [29,75,80,10,31]

for draw in range(0, 90):
	drawNumber = draw + 1
	thisWeeksDraw = GetDrawNumbers()
	numbersMatched = CheckNumbers(myNumbers, thisWeeksDraw)
	drawMatchedNumbers = DrawMatchedNumbers(myNumbers, thisWeeksDraw) 
	if numbersMatched == 2:
		print("week " + str(drawNumber) + " numbers : " + str(thisWeeksDraw) + " (" + str(numbersMatched) + " matched)" + " " + str(drawMatchedNumbers))

endTime = time.perf_counter()
elapsedTime = endTime - startTime
print(" ")
print("Completed in " + str(elapsedTime) + " seconds")
