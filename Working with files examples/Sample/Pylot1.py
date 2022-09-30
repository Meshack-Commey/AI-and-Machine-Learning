import random

def pick_five_numbers():
	available_numbers = list(range(1,91))
	ticket = [ ]
	for ticket_number in range(5):
		pick_number = random.choice(available_numbers)
		ticket.append(pick_number)
		available_numbers.remove(pick_number)
	return ticket

my_ticket = pick_five_numbers()
print(my_ticket)

