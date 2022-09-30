import os
import time, datetime, random, string
import numpy as np

#Generator Class
class Machine:
	#Machine Time
	Machinetime = time.asctime(time.localtime(time.time()))
	print(" \n ")
	print("\t ", "------------------------------------------")
	print("\t         ", Machinetime)

	
	#Clear existing data from MachineTickets.csv file
	#os.remove("MachineTickets.csv")
	
	#Set Run Time
	print("\t","-------------------------------------------")
	runtime = int(input("\t         Set Run Time (in seconds): "))
	

	#Generate new data into MachineTickets.csv file
	print("\t ","------------------------------------------")
	print("\t "," |","Keys","|","        Machine Tickets")
	print("\t ","------------------------------------------")
	for machineKeys in range(1, 16): #Ticket will loop 15 times
		def pick_five_numbers(): #Ticket loop function
			available_numbers = list(range(1,91)) #List of numbers from 1 to 90
			ticket = [ ] #Machine ticket
			for ticket_number in range(5):
				pick_number = random.choice(available_numbers)
				ticket.append(pick_number)
				available_numbers.remove(pick_number)
			return ticket #return Draws
		
		xTickets = pick_five_numbers()
		Ticketware = { machineKeys : xTickets }
		"""if machineKeys = 1:
			xTicket1 = { 1 : Ticketware[machineKeys] }
		if machineKeys = 2:
			xTicket2 = { 2 : Ticketware[machineKeys] }
		if machineKeys = 3:
			xTicket3 = { 3 : Ticketware[machineKeys] } """
			
		print("\t ", " |", machineKeys,"   | ", xTickets[0]," , ",xTickets[1]," , ",xTickets[2]," , ",xTickets[3]," , ",xTickets[4])#Prints the machine tickets on Screen
		
		#tuple = (" |", machineKeys,"   | ", xTickets[0]," , ",xTickets[1]," , ",xTickets[2]," , ",xTickets[3]," , ",xTickets[4])
		
		#print(tuple)
		
		#Machine Tickets data file
		with open("MachineTickets.csv", "a+") as file:
			Ticketwarehouse = [ ]
			Ticketwarehouse.append(xTickets)
			file.writelines(str(Ticketwarehouse)) #write into file
			
		# Store xTickets in a numpy data file
			#saved = np.array(xTickets)
			#np.save("xTickets", saved)
		
		time.sleep(runtime) #Each Element will be printed/stored after 90 seconds
	print("\t ", "------------------------------------------")
	
	print(" \n ")

"""
#Read Tickets Class
class ReadTickets:
	#Read from MachineTickets.csv file
	with open("MachineTickets.csv", "r") as file:
		y = file.readline()
		M = np.asarray(y)
		MacTick = np.arange(90)
		
		print(MacTick)
		
		#Read Tickets from numpy data file
		
"""
"""
class elementFreq(Machine, ReadTickets):
	#Initialize array
	#x = Machine.Ticketware
	#y = Machine.machineKeys
	#z = Machine.xTickets
	v = ReadTickets.MacTick
	
	print(" ")
	arr = [ v, None] 
	#Array frequency will store frequencies of element    
	frequency = [None] * len(arr)    
	visited = -1
	
	for i in range(0, len(arr)):
	    	count = 1
	    	for j in range(i+1, len(arr)):
	    			if(arr[i] == arr[j]):
	    				count = count + 1
	    				#To avoid counting same element again
	    				frequency[j] = visited
	    			if(frequency[i] != visited):
	    				frequency[i] = count
	#Displays the frequency of each element present in array
	print("---------------------")
	print(" Element | Frequency")
	print("---------------------")
	
	for i in range(0, len(frequency)):
    			if(frequency[i] != visited):
    				print("    " + str(arr[i]) + "    |    " + str(frequency[i]))
    				print("---------------------")  
"""


	
