import time, random

def pick_five():
	avail = list(range(1, 91))
	ticket = [ ]
	for i in range(5):
		pick = random.choice(avail)
		ticket.append(pick)
		avail.remove(pick)
	return ticket

my_ticket = [74, 77, 5, 33, 8] #pick_five()
#print(my_ticket)


win_condition = False
game_count = 0

while win_condition is False:
	game_count += 1
	winning_numbers = pick_five()
	
	if winning_numbers == my_ticket:
		total_cost = game_count * 1
		total_weeks = game_count / 2
		total_years = round(total_weeks/52, 1)
		
		print("You've won! and it only took {:,} games".format(game_count))
		print("total cost: GH¢{:,}".format(total_cost))
		print("total weeks: {:,} weeks".format(total_weeks))
		print("total_years: {:,} years".format(total_years))
		win_condition = True
	
	#if game_count % 10000== 0:
		#print("\r","Game : {:,}".format(game_count), end="")
 
 
 
 
 