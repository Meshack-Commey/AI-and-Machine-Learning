import pandas as pd
import numpy as np
import string, time


#df = pd.DataFrame({'col1':[74, 77, 5, 33, 8], 'col2':[70, 50, 35, 59, 34], 'col3': [3, 4, 14, 12, 64]}, index=[1, 2,3])

#df = pd.DataFrame(data, index, columns, dtype, copy)

"""
for machineKeys in range(1, 6):
			def pick_five_numbers():
				#Ticket loop function
				available_numbers = list(range(1,91))
				#List of numbers from 1 to 90
				ticket = [ ] #Machine ticket
				for ticket_number in range(5):
					pick_number = np.random.choice(available_numbers)
					ticket.append(pick_number)
					available_numbers.remove(pick_number)
				return ticket #return Draws
			xTickets = pick_five_numbers()
			#print(xTickets)
			Ticketware = { machineKeys : xTickets }
			print(Ticketware)
			time.sleep(1)
			#pandas
df = pd.DataFrame(xTickets, index=[1,2,3,4,5], )
print(df)
			#time.sleep(1)

#df = pd.DataFrame()
"""

df = pd.DataFrame([[1,2,3,4,5],[8,7,6,3,5],[4,3,2,1,4], [8,7,9,5,2], [5,4,3,2,1]],
 index=['b1','b2','b3','b4', 'b5'], 
 columns=['1st Ball', '2nd Ball', '3rd Ball', '4th Ball', '5th Ball'])

print(df)