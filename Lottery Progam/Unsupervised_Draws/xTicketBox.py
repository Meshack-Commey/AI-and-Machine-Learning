import numpy as np
import pandas as pd
import time



runtime = 1
#int(input("Set Run Time (in seconds): "))
print(" ")

#############################

def xTicket():
				available_numbers = list(range(1,91))
				ticket = [ ]
				for ticket_number in range(5):
					pick_number = np.random.choice(available_numbers)
					ticket.append(pick_number)
					available_numbers.remove(pick_number)
				return ticket #return ticket


##########################		
	
#Ticket will run at 60 seconds time
class RunTicket:
	def ticket1():
		for i in range(1):
			ticket1 = xTicket()
			#print(ticket1)
			time.sleep(runtime)
		return ticket1
	def ticket2():
		for i in range(1):
			ticket2 = xTicket()
			#print(ticket2)
			time.sleep(runtime)
		return ticket2
	def ticket3():
		for i in range(1):
			ticket3 = xTicket()
			#print(ticket3)
			time.sleep(runtime)
		return ticket3
	def ticket4():
		for i in range(1):
			ticket4 = xTicket()
			#print(ticket4)
			time.sleep(runtime)
		return ticket4
	def ticket5():
		for i in range(1):
			ticket5 = xTicket()
			#print(ticket5)
			time.sleep(runtime)
		return ticket5
	def ticket6():
		for i in range(1):
			ticket6 = xTicket()
			#print(ticket6)
			time.sleep(runtime)
		return ticket6
	def ticket7():
		for i in range(1):
			ticket7 = xTicket()
			#print(ticket7)
			time.sleep(runtime)
		return ticket7
	def ticket8():
		for i in range(1):
			ticket8 = xTicket()
			#print(ticket8)
			time.sleep(runtime)
		return ticket8
	def ticket9():
		for i in range(1):
			ticket9 = xTicket()
			#print(ticket9)
			time.sleep(runtime)
		return ticket9
	def ticket10():
		for i in range(1):
			ticket10 = xTicket()
			#print(ticket10)
			time.sleep(runtime)
		return ticket10
	def ticket11():
		for i in range(1):
			ticket11 = xTicket()
			#print(ticket11)
			time.sleep(runtime)
		return ticket11
	def ticket12():
		for i in range(1):
			ticket12 = xTicket()
			#print(ticket12)
			time.sleep(runtime)
		return ticket12
	def ticket13():
		for i in range(1):
			ticket13 = xTicket()
			#print(ticket13)
			time.sleep(runtime)
		return ticket13
	def ticket14():
		for i in range(1):
			ticket14 = xTicket()
			#print(ticket14)
			time.sleep(runtime)
		return ticket14
	def ticket15():
		for i in range(1):
			ticket15 = xTicket()
			#print(ticket15)
			time.sleep(runtime)
		return ticket15
		
############################

#Display Tickets
T1 = RunTicket.ticket1()
print(T1)
T2 = RunTicket.ticket2()
print(T2)
T3 = RunTicket.ticket3()
print(T3)
T4 = RunTicket.ticket4()
print(T4)
T5 = RunTicket.ticket5()
print(T5)
T6 = RunTicket.ticket6()
print(T6)
T7 = RunTicket.ticket7()
print(T7)
T8 = RunTicket.ticket8()
print(T8)
T9 = RunTicket.ticket9()
print(T9)
T10 = RunTicket.ticket10()
print(T10)
T11 = RunTicket.ticket11()
print(T11)
T12 = RunTicket.ticket12()
print(T12)
T13 = RunTicket.ticket13()
print(T13)
T14 = RunTicket.ticket14()
print(T14)
T15 = RunTicket.ticket15()
print(T15)

#print(T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15)
"""
#Pandas DataFrame
df = pd.DataFrame([T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15], index = ['T1','T2','T3','T4','T5', 'T6', 'T7', 'T8', 'T9', 'T10', 'T11', 'T12', 'T13', 'T14', 'T15'], columns = ['1st', '2nd', '3rd', '4th', '5th'])
#print(df)
print("\n")
"""
#Numpy ndarray
"""
nd = np.array([T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15])
print(nd.reshape(3, 5, 5))
"""

##############################
#Frequency of Ticket Balls

ms = [T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15]    

arr = [
 # ball 1, #ball 2, #ball 3,   #ball 4, #ball 5
ms[0][0], ms[0][1],ms[0][2],ms[0][3],ms[0][4], 
ms[1][0], ms[1][1],ms[1][2],ms[1][3],ms[1][4], 
ms[2][0],ms[2][1],ms[2][2],ms[2][3],ms[2][4],
ms[3][0],ms[3][1],ms[3][2],ms[3][3],ms[3][4], 
ms[4][0],ms[4][1],ms[4][2],ms[4][3],ms[4][4],
ms[5][0],ms[5][1],ms[5][2],ms[5][3],ms[5][4],
ms[6][0],ms[6][1],ms[6][2],ms[6][3],ms[6][4], 
ms[7][0],ms[7][1],ms[7][2],ms[7][3],ms[7][4], 
ms[8][0],ms[8][1],ms[8][2],ms[8][3],ms[8][4],
ms[9][0],ms[9][1],ms[9][2],ms[9][3],ms[9][4],
ms[10][0],ms[10][1],ms[10][2],ms[10][3],ms[10][4],
ms[11][0],ms[11][1],ms[11][2],ms[11][3],ms[11][4],
ms[12][0],ms[12][1],ms[12][2],ms[12][3],ms[12][4], 
ms[13][0],ms[13][1],ms[13][2],ms[13][3],ms[13][4], 
ms[14][0],ms[14][1],ms[14][2],ms[14][3],ms[14][4]
		]

#Array fr will store frequencies of element

fr = [None] * len(arr) 
visited = -1

for i in range(0, len(arr)):    
    count = 1
    for j in range(i+1, len(arr)):    
        if(arr[i] == arr[j]):    
            count = count + 1
            #To avoid counting same element again   
            fr[j] = visited
    if(fr[i] != visited):    
        fr[i] = count

#Displays the frequency of each element present in array    
print(" \n ")
print("---------------------")
print(" Balls    | Frequency")
print("---------------------");    
for i in range(0, len(fr)):    
    if(fr[i] != visited):
        eball = str(arr[i])
        efreq = str(fr[i])
        print("    " + eball + "    |    " + efreq)
print("---------------------")
print("\n")

"""
#Displays the frequency of each element present in all the xTickets array on Pandas DataFrame
for i in range(0, len(fr)):
  if(fr[i] != visited):
  	freq = np.array([[str(arr[i])], [str(fr[i])]])
  	print(freq)
  
"""

#Balls that occurs n number of times
class Occurrance:
		def Once():
			for i in range(0, len(fr)):
				if(fr[i] == 1):
						once = int(arr[i])
						print(once, end=", ")
							
		def Twice():
			for i in range(0, len(fr)):
				if(fr[i] == 2):
					twice = int(arr[i])
					twiceList = [ ]
					twiceList.append(twice)
					print(twiceList, end=", ")
		
		def Thrice():
			for i in range(0, len(fr)):
				if(fr[i] == 3):
					thrice = int(arr[i])
					print(thrice, end=", ")
		
		def Four():
			for i in range(0, len(fr)):
				if(fr[i] == 4):
					four = int(arr[i])
					print(four, end =", ")
		
		def Five():
			for i in range(0, len(fr)):
				if(fr[i] == 5):
					five = int(arr[i])
					print(five, end=" ")
		
		def Six():
			for i in range(0, len(fr)):
				if(fr[i] == 6):
					six = int(arr[i])
					print(six, end=", ")

#######################################################################
print("-------------------------------------------------------")
print("Balls which occurred Once \n ")
Occurrance.Once()

print(" \n \n ")
print("-------------------------------------------------------")

print("Balls which occurred Twice \n ")
Occurrance.Twice()

print("\n \n")
print('-------------------------------------------------------')
print("Balls which occurred Thrice \n ")
Occurrance.Thrice()
print("\n \n")
print("-------------------------------------------------------")
print("Balls which occurred Four times \n")
Occurrance.Four()
print("\n \n")
print("-------------------------------------------------------")
print("Balls which occurred Five times \n ")
Occurrance.Five()
print("\n \n")
print("-------------------------------------------------------")
print("Balls which occurred Six times \n ")
Occurrance.Six()
print("\n \n")
print("-------------------------------------------------------")




###################################################################
t0 = [
ms[0][0],ms[0][1],ms[0][2],ms[0][3],ms[0][4]
]
t1 = [
ms[1][0],ms[1][1],ms[1][2],ms[1][3],ms[1][4]
]
t2 = [
ms[2][0],ms[2][1],ms[2][2],ms[2][3],ms[2][4]
]
t3 = [
ms[3][0],ms[3][1],ms[3][2],ms[3][3],ms[3][4]
]
t4 = [
ms[4][0],ms[4][1],ms[4][2],ms[4][3],ms[4][4] ]
t5 = [
ms[5][0],ms[5][1],ms[5][2],ms[5][3],ms[5][4]
]
t6 = [
ms[6][0],ms[6][1],ms[6][2],ms[6][3],ms[6][4] 
]
t7 = [
ms[7][0],ms[7][1],ms[7][2],ms[7][3],ms[7][4] 
]
t8 = [
ms[8][0],ms[8][1],ms[8][2],ms[8][3],ms[8][4]
]
t9 = [
ms[9][0],ms[9][1],ms[9][2],ms[9][3],ms[9][4]
]
t10 = [
ms[10][0],ms[10][1],ms[10][2],ms[10][3],ms[10][4]
]
t11 = [
ms[11][0],ms[11][1],ms[11][2],ms[11][3],ms[11][4]
]
t12 = [
ms[12][0],ms[12][1],ms[12][2],ms[12][3],ms[12][4]
]
t13 = [
ms[13][0],ms[13][1],ms[13][2],ms[13][3],ms[13][4]
]
t14 = [
ms[14][0],ms[14][1],ms[14][2],ms[14][3],ms[14][4]
		]

########################################################
AppendList = [ ]

##############################################
#Ticket 0 & 1
if t0[0]==t1[0] or t0[0]==t1[1] or t0[0]==t1[2] or t0[0]==t1[3] or t0[0]==t1[4]:
 print(t0[0])
 AppendList.append(t0[0])
if t0[1]==t1[0] or t0[1]==t1[1] or t0[1]==t1[2] or t0[1]==t1[3] or t0[1]==t1[4]:
 print(t0[1])
 AppendList.append(t0[1])
if t0[2]==t1[0] or t0[2]==t1[1] or t0[2]==t1[2] or t0[2]==t1[3] or t0[2]==t1[4]:
 print(t0[2])
 AppendList.append(t0[2])
if t0[3]==t1[0] or t0[3]==t1[1] or t0[3]==t1[2] or t0[3]==t1[3] or t0[3]==t1[4]:
 print(t0[3])
 AppendList.append(t0[3])
if t0[4]==t1[0] or t0[4]==t1[1] or t0[4]==t1[2] or t0[4]==t1[3] or t0[4]==t1[4]:
 print(t0[4])
 AppendList.append(t0[4])

#Ticket 0 & 2
if t0[0]==t2[0] or t0[0]==t2[1] or t0[0]==t2[2] or t0[0]==t2[3] or t0[0]==t2[4]:
 print(t0[0])
 AppendList.append(t0[0])
if t0[1]==t2[0] or t0[1]==t2[1] or t0[1]==t2[2] or t0[1]==t2[3] or t0[1]==t2[4]:
 print(t0[1])
 AppendList.append(t0[1])
if t0[2]==t2[0] or t0[2]==t2[1] or t0[2]==t2[2] or t0[2]==t2[3] or t0[2]==t2[4]:
 print(t0[2])
 AppendList.append(t0[2])
if t0[3]==t2[0] or t0[3]==t2[1] or t0[3]==t2[2] or t0[3]==t2[3] or t0[3]==t2[4]:
 print(t0[3])
 AppendList.append(t0[3])
if t0[4]==t2[0] or t0[4]==t2[1] or t0[4]==t2[2] or t0[4]==t2[3] or t0[4]==t2[4]:
 print(t0[4])
 AppendList.append(t0[4])

#Ticket 0 & 3
if t0[0]==t3[0] or t0[0]==t3[1] or t0[0]==t3[2] or t0[0]==t3[3] or t0[0]==t3[4]:
 print(t0[0])
 AppendList.append(t0[0])
if t0[1]==t3[0] or t0[1]==t3[1] or t0[1]==t3[2] or t0[1]==t3[3] or t0[1]==t3[4]:
 print(t0[1])
 AppendList.append(t0[1])
if t0[2]==t3[0] or t0[2]==t3[1] or t0[2]==t3[2] or t0[2]==t3[3] or t0[2]==t2[4]:
 print(t0[2])
 AppendList.append(t0[2])
if t0[3]==t3[0] or t0[3]==t3[1] or t0[3]==t3[2] or t0[3]==t3[3] or t0[3]==t3[4]:
 print(t0[3])
 AppendList.append(t0[3])
if t0[4]==t3[0] or t0[4]==t3[1] or t0[4]==t3[2] or t0[4]==t3[3] or t0[4]==t3[4]:
 print(t0[4])
 AppendList.append(t0[4])

#Ticket 0 & 4
if t0[0]==t4[0] or t0[0]==t4[1] or t0[0]==t4[2] or t0[0]==t4[3] or t0[0]==t4[4]:
 print(t0[0])
 AppendList.append(t0[0])
if t0[1]==t4[0] or t0[1]==t4[1] or t0[1]==t4[2] or t0[1]==t4[3] or t0[1]==t4[4]:
 print(t0[1])
 AppendList.append(t0[1])
if t0[2]==t4[0] or t0[2]==t4[1] or t0[2]==t4[2] or t0[2]==t4[3] or t0[2]==t4[4]:
 print(t0[2])
 AppendList.append(t0[2])
if t0[3]==t4[0] or t0[3]==t4[1] or t0[3]==t4[2] or t0[3]==t4[3] or t0[3]==t4[4]:
 print(t0[3])
 AppendList.append(t0[3])
if t0[4]==t4[0] or t0[4]==t4[1] or t0[4]==t4[2] or t0[4]==t4[3] or t0[4]==t4[4]:
 print(t0[4])
 AppendList.append(t0[4])
 
 #Ticket 0 & 5
if t0[0]==t5[0] or t0[0]==t5[1] or t0[0]==t5[2] or t0[0]==t5[3] or t0[0]==t5[4]:
 print(t0[0])
 AppendList.append(t0[0])
if t0[1]==t5[0] or t0[1]==t5[1] or t0[1]==t5[2] or t0[1]==t5[3] or t0[1]==t5[4]:
 print(t0[1])
 AppendList.append(t0[1])
if t0[2]==t5[0] or t0[2]==t5[1] or t0[2]==t5[2] or t0[2]==t5[3] or t0[2]==t5[4]:
 print(t0[2])
 AppendList.append(t0[2])
if t0[3]==t5[0] or t0[3]==t5[1] or t0[3]==t5[2] or t0[3]==t5[3] or t0[3]==t5[4]:
 print(t0[3])
 AppendList.append(t0[3])
if t0[4]==t5[0] or t0[4]==t5[1] or t0[4]==t5[2] or t0[4]==t5[3] or t0[4]==t5[4]:
 print(t0[4])
 AppendList.append(t0[4])
 
 #Ticket 0 & 6
if t0[0]==t6[0] or t0[0]==t6[1] or t0[0]==t6[2] or t0[0]==t6[3] or t0[0]==t6[4]:
 print(t0[0])
 AppendList.append(t0[0])
if t0[1]==t6[0] or t0[1]==t6[1] or t0[1]==t6[2] or t0[1]==t6[3] or t0[1]==t6[4]:
 print(t0[1])
 AppendList.append(t0[1])
if t0[2]==t6[0] or t0[2]==t6[1] or t0[2]==t6[2] or t0[2]==t6[3] or t0[2]==t6[4]:
 print(t0[2])
 AppendList.append(t0[2])
if t0[3]==t6[0] or t0[3]==t6[1] or t0[3]==t6[2] or t0[3]==t6[3] or t0[3]==t6[4]:
 print(t0[3])
 AppendList.append(t0[3])
if t0[4]==t6[0] or t0[4]==t6[1] or t0[4]==t6[2] or t0[4]==t6[3] or t0[4]==t6[4]:
 print(t0[4])
 AppendList.append(t0[4])
 
#Ticket 0 & 7
if t0[0]==t7[0] or t0[0]==t7[1] or t0[0]==t7[2] or t0[0]==t7[3] or t0[0]==t7[4]:
 print(t0[0])
 AppendList.append(t0[0])
if t0[1]==t7[0] or t0[1]==t7[1] or t0[1]==t7[2] or t0[1]==t7[3] or t0[1]==t7[4]:
 print(t0[1])
 AppendList.append(t0[1])
if t0[2]==t7[0] or t0[2]==t7[1] or t0[2]==t7[2] or t0[2]==t7[3] or t0[2]==t7[4]:
 print(t0[2])
 AppendList.append(t0[2])
if t0[3]==t7[0] or t0[3]==t7[1] or t0[3]==t7[2] or t0[3]==t7[3] or t0[3]==t7[4]:
 print(t0[3])
 AppendList.append(t0[3])
if t0[4]==t7[0] or t0[4]==t7[1] or t0[4]==t7[2] or t0[4]==t7[3] or t0[4]==t7[4]:
 print(t0[4])
 AppendList.append(t0[4])
 
#Ticket 0 & 8
if t0[0]==t8[0] or t0[0]==t8[1] or t0[0]==t8[2] or t0[0]==t8[3] or t0[0]==t8[4]:
 print(t0[0])
 AppendList.append(t0[0])
if t0[1]==t8[0] or t0[1]==t8[1] or t0[1]==t8[2] or t0[1]==t8[3] or t0[1]==t8[4]:
 print(t0[1])
 AppendList.append(t0[1])
if t0[2]==t8[0] or t0[2]==t8[1] or t0[2]==t8[2] or t0[2]==t8[3] or t0[2]==t8[4]:
 print(t0[2])
 AppendList.append(t0[2])
if t0[3]==t8[0] or t0[3]==t8[1] or t0[3]==t8[2] or t0[3]==t8[3] or t0[3]==t8[4]:
 print(t0[3])
 AppendList.append(t0[3])
if t0[4]==t8[0] or t0[4]==t8[1] or t0[4]==t8[2] or t0[4]==t8[3] or t0[4]==t8[4]:
 print(t0[4])
 AppendList.append(t0[4])

#Ticket 0 & 9
if t0[0]==t9[0] or t0[0]==t9[1] or t0[0]==t9[2] or t0[0]==t9[3] or t0[0]==t9[4]:
 print(t0[0])
 AppendList.append(t0[0])
if t0[1]==t9[0] or t0[1]==t9[1] or t0[1]==t9[2] or t0[1]==t9[3] or t0[1]==t9[4]:
 print(t0[1])
 AppendList.append(t0[1])
if t0[2]==t9[0] or t0[2]==t9[1] or t0[2]==t9[2] or t0[2]==t9[3] or t0[2]==t9[4]:
 print(t0[2])
 AppendList.append(t0[2])
if t0[3]==t9[0] or t0[3]==t9[1] or t0[3]==t9[2] or t0[3]==t9[3] or t0[3]==t9[4]:
 print(t0[3])
 AppendList.append(t0[3])
if t0[4]==t9[0] or t0[4]==t9[1] or t0[4]==t9[2] or t0[4]==t9[3] or t0[4]==t9[4]:
 print(t0[4])
 AppendList.append(t0[4])

 #Ticket 0 & 10
if t0[0]==t10[0] or t0[0]==t10[1] or t0[0]==t10[2] or t0[0]==t10[3] or t0[0]==t10[4]:
 print(t0[0])
 AppendList.append(t0[0])
if t0[1]==t10[0] or t0[1]==t10[1] or t0[1]==t10[2] or t0[1]==t10[3] or t0[1]==t10[4]:
 print(t0[1])
 AppendList.append(t0[1])
if t0[2]==t10[0] or t0[2]==t10[1] or t0[2]==t10[2] or t0[2]==t10[3] or t0[2]==t10[4]:
 print(t0[2])
 AppendList.append(t0[2])
if t0[3]==t10[0] or t0[3]==t10[1] or t0[3]==t10[2] or t0[3]==t10[3] or t0[3]==t10[4]:
 print(t0[3])
 AppendList.append(t0[3])
if t0[4]==t10[0] or t0[4]==t10[1] or t0[4]==t10[2] or t0[4]==t10[3] or t0[4]==t10[4]:
 print(t0[4])
 AppendList.append(t0[4])
 
#Ticket 0 & 11
if t0[0]==t11[0] or t0[0]==t11[1] or t0[0]==t11[2] or t0[0]==t11[3] or t0[0]==t11[4]:
 print(t0[0])
 AppendList.append(t0[0])
if t0[1]==t11[0] or t0[1]==t11[1] or t0[1]==t11[2] or t0[1]==t11[3] or t0[1]==t11[4]:
 print(t0[1])
 AppendList.append(t0[1])
if t0[2]==t11[0] or t0[2]==t11[1] or t0[2]==t11[2] or t0[2]==t11[3] or t0[2]==t11[4]:
 print(t0[2])
 AppendList.append(t0[2])
if t0[3]==t11[0] or t0[3]==t11[1] or t0[3]==t11[2] or t0[3]==t11[3] or t0[3]==t11[4]:
 print(t0[3])
 AppendList.append(t0[3])
if t0[4]==t11[0] or t0[4]==t11[1] or t0[4]==t11[2] or t0[4]==t11[3] or t0[4]==t11[4]:
 print(t0[4])
 AppendList.append(t0[4])
 
#Ticket 0 & 12
if t0[0]==t12[0] or t0[0]==t12[1] or t0[0]==t12[2] or t0[0]==t12[3] or t0[0]==t12[4]:
 print(t0[0])
 AppendList.append(t0[0])
if t0[1]==t12[0] or t0[1]==t12[1] or t0[1]==t12[2] or t0[1]==t12[3] or t0[1]==t12[4]:
 print(t0[1])
 AppendList.append(t0[1])
if t0[2]==t12[0] or t0[2]==t12[1] or t0[2]==t12[2] or t0[2]==t12[3] or t0[2]==t12[4]:
 print(t0[2])
 AppendList.append(t0[2])
if t0[3]==t12[0] or t0[3]==t12[1] or t0[3]==t12[2] or t0[3]==t12[3] or t0[3]==t12[4]:
 print(t0[3])
 AppendList.append(t0[3])
if t0[4]==t12[0] or t0[4]==t12[1] or t0[4]==t12[2] or t0[4]==t12[3] or t0[4]==t12[4]:
 print(t0[4])
 AppendList.append(t0[4])
 
#Ticket 0 & 13
if t0[0]==t13[0] or t0[0]==t13[1] or t0[0]==t13[2] or t0[0]==t13[3] or t0[0]==t13[4]:
 print(t0[0])
 AppendList.append(t0[0])
if t0[1]==t13[0] or t0[1]==t13[1] or t0[1]==t13[2] or t0[1]==t13[3] or t0[1]==t13[4]:
 print(t0[1])
 AppendList.append(t0[1])
if t0[2]==t13[0] or t0[2]==t13[1] or t0[2]==t13[2] or t0[2]==t13[3] or t0[2]==t13[4]:
 print(t0[2])
 AppendList.append(t0[2])
if t0[3]==t13[0] or t0[3]==t13[1] or t0[3]==t13[2] or t0[3]==t13[3] or t0[3]==t13[4]:
 print(t0[3])
 AppendList.append(t0[3])
if t0[4]==t13[0] or t0[4]==t13[1] or t0[4]==t13[2] or t0[4]==t13[3] or t0[4]==t13[4]:
 print(t0[4])
 AppendList.append(t0[4])
 
 #Ticket 0 & 14
if t0[0]==t14[0] or t0[0]==t14[1] or t0[0]==t14[2] or t0[0]==t14[3] or t0[0]==t14[4]:
 print(t0[0])
 AppendList.append(t0[0])
if t0[1]==t14[0] or t0[1]==t14[1] or t0[1]==t14[2] or t0[1]==t14[3] or t0[1]==t14[4]:
 print(t0[1])
 AppendList.append(t0[1])
if t0[2]==t14[0] or t0[2]==t14[1] or t0[2]==t14[2] or t0[2]==t14[3] or t0[2]==t14[4]:
 print(t0[2])
 AppendList.append(t0[2])
if t0[3]==t14[0] or t0[3]==t14[1] or t0[3]==t14[2] or t0[3]==t14[3] or t0[3]==t14[4]:
 print(t0[3])
 AppendList.append(t0[3])
if t0[4]==t14[0] or t0[4]==t14[1] or t0[4]==t14[2] or t0[4]==t14[3] or t0[4]==t14[4]:
 print(t0[4])
 AppendList.append(t0[4])
########### TICKET 1 ################################################

#Ticket 1 & 2
if t1[0]==t2[0] or t1[0]==t2[1] or t1[0]==t2[2] or t1[0]==t2[3] or t1[0]==t2[4]:
 print(t1[0])
 AppendList.append(t1[0])
if t1[1]==t2[0] or t1[1]==t2[1] or t1[1]==t2[2] or t1[1]==t2[3] or t1[1]==t2[4]:
 print(t1[1])
 AppendList.append(t1[1])
if t1[2]==t2[0] or t1[2]==t2[1] or t1[2]==t2[2] or t1[2]==t2[3] or t1[2]==t2[4]:
 print(t1[2])
 AppendList.append(t1[2])
if t1[3]==t2[0] or t1[3]==t2[1] or t1[3]==t2[2] or t1[3]==t2[3] or t1[3]==t2[4]:
 print(t1[3])
 AppendList.append(t1[3])
if t1[4]==t2[0] or t1[4]==t2[1] or t1[4]==t2[2] or t1[4]==t2[3] or t1[4]==t2[4]:
 print(t1[4])
 AppendList.append(t1[4])

#Ticket 1 & 3
if t1[0]==t3[0] or t1[0]==t3[1] or t1[0]==t3[2] or t1[0]==t3[3] or t1[0]==t3[4]:
 print(t1[0])
 AppendList.append(t1[0])
if t1[1]==t3[0] or t1[1]==t3[1] or t1[1]==t3[2] or t1[1]==t3[3] or t1[1]==t3[4]:
 print(t1[1])
 AppendList.append(t1[1])
if t1[2]==t3[0] or t1[2]==t3[1] or t1[2]==t3[2] or t1[2]==t3[3] or t1[2]==t2[4]:
 print(t1[2])
 AppendList.append(t1[2])
if t1[3]==t3[0] or t1[3]==t3[1] or t1[3]==t3[2] or t1[3]==t3[3] or t1[3]==t3[4]:
 print(t1[3])
 AppendList.append(t1[3])
if t1[4]==t3[0] or t1[4]==t3[1] or t1[4]==t3[2] or t1[4]==t3[3] or t1[4]==t3[4]:
 print(t1[4])
 AppendList.append(t1[4])

#Ticket 1 & 4
if t1[0]==t4[0] or t1[0]==t4[1] or t1[0]==t4[2] or t1[0]==t4[3] or t1[0]==t4[4]:
 print(t1[0])
 AppendList.append(t1[0])
if t1[1]==t4[0] or t1[1]==t4[1] or t1[1]==t4[2] or t1[1]==t4[3] or t1[1]==t4[4]:
 print(t1[1])
 AppendList.append(t1[1])
if t1[2]==t4[0] or t1[2]==t4[1] or t1[2]==t4[2] or t1[2]==t4[3] or t1[2]==t4[4]:
 print(t1[2])
 AppendList.append(t1[2])
if t1[3]==t4[0] or t1[3]==t4[1] or t1[3]==t4[2] or t1[3]==t4[3] or t1[3]==t4[4]:
 print(t1[3])
 AppendList.append(t1[3])
if t1[4]==t4[0] or t1[4]==t4[1] or t1[4]==t4[2] or t1[4]==t4[3] or t1[4]==t4[4]:
 print(t1[4])
 AppendList.append(t1[4])

 #Ticket 1 & 5
if t1[0]==t5[0] or t1[0]==t5[1] or t1[0]==t5[2] or t1[0]==t5[3] or t1[0]==t5[4]:
 print(t1[0])
 AppendList.append(t1[0])
if t1[1]==t5[0] or t1[1]==t5[1] or t1[1]==t5[2] or t1[1]==t5[3] or t1[1]==t5[4]:
 print(t1[1])
 AppendList.append(t1[1])
if t1[2]==t5[0] or t1[2]==t5[1] or t1[2]==t5[2] or t1[2]==t5[3] or t1[2]==t5[4]:
 print(t1[2])
 AppendList.append(t1[2])
if t1[3]==t5[0] or t1[3]==t5[1] or t1[3]==t5[2] or t1[3]==t5[3] or t1[3]==t5[4]:
 print(t1[3])
 AppendList.append(t1[3])
if t1[4]==t5[0] or t1[4]==t5[1] or t1[4]==t5[2] or t1[4]==t5[3] or t1[4]==t5[4]:
 print(t1[4])
 AppendList.append(t1[4])
 
 #Ticket 1 & 6
if t1[0]==t6[0] or t1[0]==t6[1] or t1[0]==t6[2] or t1[0]==t6[3] or t1[0]==t6[4]:
 print(t1[0])
 AppendList.append(t1[0])
if t1[1]==t6[0] or t1[1]==t6[1] or t1[1]==t6[2] or t1[1]==t6[3] or t1[1]==t6[4]:
 print(t1[1])
 AppendList.append(t1[1])
if t1[2]==t6[0] or t1[2]==t6[1] or t1[2]==t6[2] or t1[2]==t6[3] or t1[2]==t6[4]:
 print(t1[2])
 AppendList.append(t1[2])
if t1[3]==t6[0] or t1[3]==t6[1] or t1[3]==t6[2] or t1[3]==t6[3] or t1[3]==t6[4]:
 print(t1[3])
 AppendList.append(t1[3])
if t1[4]==t6[0] or t1[4]==t6[1] or t1[4]==t6[2] or t1[4]==t6[3] or t1[4]==t6[4]:
 print(t1[4])
 AppendList.append(t1[4])
 
#Ticket 1 & 7
if t1[0]==t7[0] or t1[0]==t7[1] or t1[0]==t7[2] or t1[0]==t7[3] or t1[0]==t7[4]:
 print(t1[0])
 AppendList.append(t1[0])
if t1[1]==t7[0] or t1[1]==t7[1] or t1[1]==t7[2] or t1[1]==t7[3] or t1[1]==t7[4]:
 print(t1[1])
 AppendList.append(t1[1])
if t1[2]==t7[0] or t1[2]==t7[1] or t1[2]==t7[2] or t1[2]==t7[3] or t1[2]==t7[4]:
 print(t1[2])
 AppendList.append(t1[2])
if t1[3]==t7[0] or t1[3]==t7[1] or t1[3]==t7[2] or t1[3]==t7[3] or t1[3]==t7[4]:
 print(t1[3])
 AppendList.append(t1[3])
if t1[4]==t7[0] or t1[4]==t7[1] or t1[4]==t7[2] or t1[4]==t7[3] or t1[4]==t7[4]:
 print(t1[4])
 AppendList.append(t1[4])
 
#Ticket 1 & 8
if t1[0]==t8[0] or t1[0]==t8[1] or t1[0]==t8[2] or t1[0]==t8[3] or t1[0]==t8[4]:
 print(t1[0])
 AppendList.append(t1[0])
if t1[1]==t8[0] or t1[1]==t8[1] or t1[1]==t8[2] or t1[1]==t8[3] or t1[1]==t8[4]:
 print(t1[1])
 AppendList.append(t1[1])
if t1[2]==t8[0] or t1[2]==t8[1] or t1[2]==t8[2] or t1[2]==t8[3] or t1[2]==t8[4]:
 print(t1[2])
 AppendList.append(t1[2])
if t1[3]==t8[0] or t1[3]==t8[1] or t1[3]==t8[2] or t1[3]==t8[3] or t1[3]==t8[4]:
 print(t1[3])
 AppendList.append(t1[3])
if t1[4]==t8[0] or t1[4]==t8[1] or t1[4]==t8[2] or t1[4]==t8[3] or t1[4]==t8[4]:
 print(t1[4])
 AppendList.append(t1[4])

#Ticket 1 & 9
if t1[0]==t9[0] or t1[0]==t9[1] or t1[0]==t9[2] or t1[0]==t9[3] or t1[0]==t9[4]:
 print(t1[0])
 AppendList.append(t1[0])
if t1[1]==t9[0] or t1[1]==t9[1] or t1[1]==t9[2] or t1[1]==t9[3] or t1[1]==t9[4]:
 print(t1[1])
 AppendList.append(t1[1])
if t1[2]==t9[0] or t1[2]==t9[1] or t1[2]==t9[2] or t1[2]==t9[3] or t1[2]==t9[4]:
 print(t1[2])
 AppendList.append(t1[2])
if t1[3]==t9[0] or t1[3]==t9[1] or t1[3]==t9[2] or t1[3]==t9[3] or t1[3]==t9[4]:
 print(t1[3])
 AppendList.append(t1[3])
if t1[4]==t9[0] or t1[4]==t9[1] or t1[4]==t9[2] or t1[4]==t9[3] or t1[4]==t9[4]:
 print(t1[4])
 AppendList.append(t1[4])
 
#Ticket 1 & 10
if t1[0]==t10[0] or t1[0]==t10[1] or t1[0]==t10[2] or t1[0]==t10[3] or t1[0]==t10[4]:
 print(t1[0])
 AppendList.append(t1[0])
if t1[1]==t10[0] or t1[1]==t10[1] or t1[1]==t10[2] or t1[1]==t10[3] or t1[1]==t10[4]:
 print(t1[1])
 AppendList.append(t1[1])
if t1[2]==t10[0] or t1[2]==t10[1] or t1[2]==t10[2] or t1[2]==t10[3] or t1[2]==t10[4]:
 print(t1[2])
 AppendList.append(t1[2])
if t1[3]==t10[0] or t1[3]==t10[1] or t1[3]==t10[2] or t1[3]==t10[3] or t1[3]==t10[4]:
 print(t1[3])
 AppendList.append(t1[3])
if t1[4]==t10[0] or t1[4]==t10[1] or t1[4]==t10[2] or t1[4]==t10[3] or t1[4]==t10[4]:
 print(t1[4])
 AppendList.append(t1[4])
 
#Ticket 1 & 11
if t1[0]==t11[0] or t1[0]==t11[1] or t1[0]==t11[2] or t1[0]==t11[3] or t1[0]==t11[4]:
 print(t1[0])
 AppendList.append(t1[0])
if t1[1]==t11[0] or t1[1]==t11[1] or t1[1]==t11[2] or t1[1]==t11[3] or t1[1]==t11[4]:
 print(t1[1])
 AppendList.append(t1[1])
if t1[2]==t11[0] or t1[2]==t11[1] or t1[2]==t11[2] or t1[2]==t11[3] or t1[2]==t11[4]:
 print(t1[2])
 AppendList.append(t1[2])
if t1[3]==t11[0] or t1[3]==t11[1] or t1[3]==t11[2] or t1[3]==t11[3] or t1[3]==t11[4]:
 print(t1[3])
 AppendList.append(t1[3])
if t1[4]==t11[0] or t1[4]==t11[1] or t1[4]==t11[2] or t1[4]==t11[3] or t1[4]==t11[4]:
 print(t1[4])
 AppendList.append(t1[4])
 
#Ticket 1 & 12
if t1[0]==t12[0] or t1[0]==t12[1] or t1[0]==t12[2] or t1[0]==t12[3] or t1[0]==t12[4]:
 print(t1[0])
 AppendList.append(t1[0])
if t1[1]==t12[0] or t1[1]==t12[1] or t1[1]==t12[2] or t1[1]==t12[3] or t1[1]==t12[4]:
 print(t1[1])
 AppendList.append(t1[1])
if t1[2]==t12[0] or t1[2]==t12[1] or t1[2]==t12[2] or t1[2]==t12[3] or t1[2]==t12[4]:
 print(t1[2])
 AppendList.append(t1[2])
if t1[3]==t12[0] or t1[3]==t12[1] or t1[3]==t12[2] or t1[3]==t12[3] or t1[3]==t12[4]:
 print(t1[3])
 AppendList.append(t1[3])
if t1[4]==t12[0] or t1[4]==t12[1] or t1[4]==t12[2] or t0[4]==t12[3] or t0[4]==t12[4]:
 print(t1[4])
 AppendList.append(t1[4])
 
#Ticket 1 & 13
if t1[0]==t13[0] or t1[0]==t13[1] or t1[0]==t13[2] or t1[0]==t13[3] or t1[0]==t13[4]:
 print(t1[0])
 AppendList.append(t1[0])
if t1[1]==t13[0] or t1[1]==t13[1] or t1[1]==t13[2] or t1[1]==t13[3] or t1[1]==t13[4]:
 print(t1[1])
 AppendList.append(t1[1])
if t1[2]==t13[0] or t1[2]==t13[1] or t1[2]==t13[2] or t1[2]==t13[3] or t1[2]==t13[4]:
 print(t1[2])
 AppendList.append(t1[2])
if t1[3]==t13[0] or t1[3]==t13[1] or t1[3]==t13[2] or t1[3]==t13[3] or t1[3]==t13[4]:
 print(t1[3])
 AppendList.append(t1[3])
if t1[4]==t13[0] or t1[4]==t13[1] or t1[4]==t13[2] or t1[4]==t13[3] or t1[4]==t13[4]:
 print(t1[4])
 AppendList.append(t1[4])
 
 #Ticket 1 & 14
if t1[0]==t14[0] or t1[0]==t14[1] or t1[0]==t14[2] or t1[0]==t14[3] or t1[0]==t14[4]:
 print(t1[0])
 AppendList.append(t1[0])
if t1[1]==t14[0] or t1[1]==t14[1] or t1[1]==t14[2] or t1[1]==t14[3] or t1[1]==t14[4]:
 print(t1[1])
 AppendList.append(t1[1])
if t1[2]==t14[0] or t1[2]==t14[1] or t1[2]==t14[2] or t1[2]==t14[3] or t1[2]==t14[4]:
 print(t1[2])
 AppendList.append(t1[2])
if t1[3]==t14[0] or t1[3]==t14[1] or t1[3]==t14[2] or t1[3]==t14[3] or t1[3]==t14[4]:
 print(t1[3])
 AppendList.append(t1[3])
if t1[4]==t14[0] or t1[4]==t14[1] or t1[4]==t14[2] or t1[4]==t14[3] or t1[4]==t14[4]:
 print(t1[4])
 AppendList.append(t1[4])

########## TICKET 2 ####################

#Ticket 2 & 3
if t2[0]==t3[0] or t2[0]==t3[1] or t2[0]==t3[2] or t2[0]==t3[3] or t2[0]==t3[4]:
 print(t2[0])
 AppendList.append(t2[0])
if t2[1]==t3[0] or t2[1]==t3[1] or t2[1]==t3[2] or t2[1]==t3[3] or t2[1]==t3[4]:
 print(t2[1])
 AppendList.append(t2[2])
if t2[2]==t3[0] or t2[2]==t3[1] or t2[2]==t3[2] or t2[2]==t3[3] or t2[2]==t2[4]:
 print(t2[2])
 AppendList.append(t2[2])
if t2[3]==t3[0] or t2[3]==t3[1] or t2[3]==t3[2] or t2[3]==t3[3] or t2[3]==t3[4]:
 print(t2[3])
 AppendList.append(t2[3])
if t2[4]==t3[0] or t2[4]==t3[1] or t2[4]==t3[2] or t2[4]==t3[3] or t2[4]==t3[4]:
 print(t2[4])
 AppendList.append(t2[4])

#Ticket 2 & 4
if t2[0]==t4[0] or t2[0]==t4[1] or t2[0]==t4[2] or t2[0]==t4[3] or t2[0]==t4[4]:
 print(t2[0])
 AppendList.append(t2[0])
if t2[1]==t4[0] or t2[1]==t4[1] or t2[1]==t4[2] or t2[1]==t4[3] or t2[1]==t4[4]:
 print(t2[1])
 AppendList.append(t2[1])
if t2[2]==t4[0] or t2[2]==t4[1] or t2[2]==t4[2] or t2[2]==t4[3] or t2[2]==t4[4]:
 print(t2[2])
 AppendList.append(t2[2])
if t2[3]==t4[0] or t2[3]==t4[1] or t2[3]==t4[2] or t2[3]==t4[3] or t2[3]==t4[4]:
 print(t2[3])
 AppendList.append(t2[3])
if t2[4]==t4[0] or t2[4]==t4[1] or t2[4]==t4[2] or t2[4]==t4[3] or t2[4]==t4[4]:
 print(t2[4])
 AppendList.append(t2[4])
 
 #Ticket 2 & 5
if t2[0]==t5[0] or t2[0]==t5[1] or t2[0]==t5[2] or t2[0]==t5[3] or t2[0]==t5[4]:
 print(t2[0])
 AppendList.append(t2[0])
if t2[1]==t5[0] or t2[1]==t5[1] or t2[1]==t5[2] or t2[1]==t5[3] or t2[1]==t5[4]:
 print(t2[1])
 AppendList.append(t2[1])
if t2[2]==t5[0] or t2[2]==t5[1] or t2[2]==t5[2] or t2[2]==t5[3] or t2[2]==t5[4]:
 print(t2[2])
 AppendList.append(t2[2])
if t2[3]==t5[0] or t2[3]==t5[1] or t2[3]==t5[2] or t2[3]==t5[3] or t2[3]==t5[4]:
 print(t2[3])
 AppendList.append(t2[3])
if t2[4]==t5[0] or t2[4]==t5[1] or t2[4]==t5[2] or t2[4]==t5[3] or t2[4]==t5[4]:
 print(t2[4])
 AppendList.append(t2[4])
 
 #Ticket 2 & 6
if t2[0]==t6[0] or t2[0]==t6[1] or t2[0]==t6[2] or t2[0]==t6[3] or t2[0]==t6[4]:
 print(t2[0])
 AppendList.append(t2[0])
if t2[1]==t6[0] or t2[1]==t6[1] or t2[1]==t6[2] or t2[1]==t6[3] or t2[1]==t6[4]:
 print(t2[1])
 AppendList.append(t2[1])
if t2[2]==t6[0] or t2[2]==t6[1] or t2[2]==t6[2] or t2[2]==t6[3] or t2[2]==t6[4]:
 print(t2[2])
 AppendList.append(t2[2])
if t2[3]==t6[0] or t2[3]==t6[1] or t2[3]==t6[2] or t2[3]==t6[3] or t2[3]==t6[4]:
 print(t2[3])
 AppendList.append(t2[3])
if t2[4]==t6[0] or t2[4]==t6[1] or t2[4]==t6[2] or t2[4]==t6[3] or t2[4]==t6[4]:
 print(t2[4])
 AppendList.append(t2[4])
 
#Ticket 2 & 7
if t2[0]==t7[0] or t2[0]==t7[1] or t2[0]==t7[2] or t2[0]==t7[3] or t2[0]==t7[4]:
 print(t2[0])
 AppendList.append(t2[0])
if t2[1]==t7[0] or t2[1]==t7[1] or t2[1]==t7[2] or t2[1]==t7[3] or t2[1]==t7[4]:
 print(t2[1])
 AppendList.append(t2[1])
if t2[2]==t7[0] or t2[2]==t7[1] or t2[2]==t7[2] or t2[2]==t7[3] or t2[2]==t7[4]:
 print(t2[2])
 AppendList.append(t2[2])
if t2[3]==t7[0] or t2[3]==t7[1] or t2[3]==t7[2] or t2[3]==t7[3] or t2[3]==t7[4]:
 print(t2[3])
 AppendList.append(t2[3])
if t2[4]==t7[0] or t2[4]==t7[1] or t2[4]==t7[2] or t2[4]==t7[3] or t2[4]==t7[4]:
 print(t2[4])
 AppendList.append(t2[4])
 
#Ticket 2 & 8
if t2[0]==t8[0] or t2[0]==t8[1] or t2[0]==t8[2] or t2[0]==t8[3] or t2[0]==t8[4]:
 print(t2[0])
 AppendList.append(t2[0])
if t2[1]==t8[0] or t2[1]==t8[1] or t2[1]==t8[2] or t2[1]==t8[3] or t2[1]==t8[4]:
 print(t2[1])
 AppendList.append(t2[1])
if t2[2]==t8[0] or t2[2]==t8[1] or t2[2]==t8[2] or t2[2]==t8[3] or t2[2]==t8[4]:
 print(t2[2])
 AppendList.append(t2[2])
if t2[3]==t8[0] or t2[3]==t8[1] or t2[3]==t8[2] or t2[3]==t8[3] or t2[3]==t8[4]:
 print(t2[3])
 AppendList.append(t2[3])
if t2[4]==t8[0] or t2[4]==t8[1] or t2[4]==t8[2] or t2[4]==t8[3] or t2[4]==t8[4]:
 print(t2[4])
 AppendList.append(t2[4])

#Ticket 2 & 9
if t2[0]==t9[0] or t2[0]==t9[1] or t2[0]==t9[2] or t2[0]==t9[3] or t2[0]==t9[4]:
 print(t2[0])
 AppendList.append(t2[0])
if t2[1]==t9[0] or t2[1]==t9[1] or t2[1]==t9[2] or t2[1]==t9[3] or t2[1]==t9[4]:
 print(t2[1])
 AppendList.append(t2[1])
if t2[2]==t9[0] or t2[2]==t9[1] or t2[2]==t9[2] or t2[2]==t9[3] or t2[2]==t9[4]:
 print(t2[2])
 AppendList.append(t2[2])
if t2[3]==t9[0] or t2[3]==t9[1] or t2[3]==t9[2] or t2[3]==t9[3] or t2[3]==t9[4]:
 print(t2[3])
 AppendList.append(t2[3])
if t2[4]==t9[0] or t2[4]==t9[1] or t2[4]==t9[2] or t2[4]==t9[3] or t2[4]==t9[4]:
 print(t2[4])
 AppendList.append(t2[4])

#Ticket 2 & 10
if t2[0]==t10[0] or t2[0]==t10[1] or t2[0]==t10[2] or t2[0]==t10[3] or t2[0]==t10[4]:
 print(t2[0])
 AppendList.append(t2[0])
if t2[1]==t10[0] or t2[1]==t10[1] or t2[1]==t10[2] or t2[1]==t10[3] or t2[1]==t10[4]:
 print(t2[1])
 AppendList.append(t2[1])
if t2[2]==t10[0] or t2[2]==t10[1] or t2[2]==t10[2] or t2[2]==t10[3] or t2[2]==t10[4]:
 print(t2[2])
 AppendList.append(t2[2])
if t2[3]==t10[0] or t2[3]==t10[1] or t2[3]==t10[2] or t2[3]==t10[3] or t2[3]==t10[4]:
 print(t2[3])
 AppendList.append(t2[3])
if t2[4]==t10[0] or t2[4]==t10[1] or t2[4]==t10[2] or t2[4]==t10[3] or t2[4]==t10[4]:
 print(t2[4])
 AppendList.append(t2[4])
 
#Ticket 2 & 11
if t2[0]==t11[0] or t2[0]==t11[1] or t2[0]==t11[2] or t2[0]==t11[3] or t2[0]==t11[4]:
 print(t2[0])
 AppendList.append(t2[0])
if t2[1]==t11[0] or t2[1]==t11[1] or t2[1]==t11[2] or t2[1]==t11[3] or t2[1]==t11[4]:
 print(t2[1])
 AppendList.append(t2[1])
if t2[2]==t11[0] or t2[2]==t11[1] or t2[2]==t11[2] or t2[2]==t11[3] or t2[2]==t11[4]:
 print(t2[2])
 AppendList.append(t2[2])
if t2[3]==t11[0] or t2[3]==t11[1] or t2[3]==t11[2] or t2[3]==t11[3] or t2[3]==t11[4]:
 print(t2[3])
 AppendList.append(t2[3])
if t2[4]==t11[0] or t2[4]==t11[1] or t2[4]==t11[2] or t2[4]==t11[3] or t2[4]==t11[4]:
 print(t2[4])
 AppendList.append(t2[4])
 
#Ticket 2 & 12
if t2[0]==t12[0] or t2[0]==t12[1] or t2[0]==t12[2] or t2[0]==t12[3] or t2[0]==t12[4]:
 print(t2[0])
 AppendList.append(t2[0])
if t2[1]==t12[0] or t2[1]==t12[1] or t2[1]==t12[2] or t2[1]==t12[3] or t2[1]==t12[4]:
 print(t2[1])
 AppendList.append(t2[1])
if t2[2]==t12[0] or t2[2]==t12[1] or t2[2]==t12[2] or t2[2]==t12[3] or t2[2]==t12[4]:
 print(t2[2])
 AppendList.append(t2[2])
if t2[3]==t12[0] or t2[3]==t12[1] or t2[3]==t12[2] or t2[3]==t12[3] or t2[3]==t12[4]:
 print(t2[3])
 AppendList.append(t2[3])
if t2[4]==t12[0] or t2[4]==t12[1] or t2[4]==t12[2] or t2[4]==t12[3] or t2[4]==t12[4]:
 print(t2[4])
 AppendList.append(t2[4])
 
#Ticket 2 & 13
if t2[0]==t13[0] or t2[0]==t13[1] or t2[0]==t13[2] or t2[0]==t13[3] or t2[0]==t13[4]:
 print(t2[0])
 AppendList.append(t2[0])
if t2[1]==t13[0] or t2[1]==t13[1] or t2[1]==t13[2] or t2[1]==t13[3] or t2[1]==t13[4]:
 print(t2[1])
 AppendList.append(t2[1])
if t2[2]==t13[0] or t2[2]==t13[1] or t2[2]==t13[2] or t2[2]==t13[3] or t2[2]==t13[4]:
 print(t2[2])
 AppendList.append(t2[2])
if t2[3]==t13[0] or t2[3]==t13[1] or t2[3]==t13[2] or t2[3]==t13[3] or t2[3]==t13[4]:
 print(t2[3])
 AppendList.append(t2[3])
if t2[4]==t13[0] or t2[4]==t13[1] or t2[4]==t13[2] or t2[4]==t13[3] or t2[4]==t13[4]:
 print(t2[4])
 AppendList.append(t2[4])
 
 #Ticket 2 & 14
if t2[0]==t14[0] or t2[0]==t14[1] or t2[0]==t14[2] or t2[0]==t14[3] or t2[0]==t14[4]:
 print(t2[0])
 AppendList.append(t2[0])
if t2[1]==t14[0] or t2[1]==t14[1] or t2[1]==t14[2] or t2[1]==t14[3] or t2[1]==t14[4]:
 print(t2[1])
 AppendList.append(t2[1])
if t2[2]==t14[0] or t2[2]==t14[1] or t2[2]==t14[2] or t2[2]==t14[3] or t2[2]==t14[4]:
 print(t2[2])
 AppendList.append(t2[2])
if t2[3]==t14[0] or t2[3]==t14[1] or t2[3]==t14[2] or t2[3]==t14[3] or t2[3]==t14[4]:
 print(t2[3])
 AppendList.append(t2[3])
if t2[4]==t14[0] or t2[4]==t14[1] or t2[4]==t14[2] or t2[4]==t14[3] or t2[4]==t14[4]:
 print(t2[4])
 AppendList.append(t2[4])

######## TICKET 3 ######################

#Ticket 3 & 4
if t3[0]==t4[0] or t3[0]==t4[1] or t3[0]==t4[2] or t3[0]==t4[3] or t3[0]==t4[4]:
 print(t3[0])
 AppendList.append(t3[0])
if t3[1]==t4[0] or t3[1]==t4[1] or t3[1]==t4[2] or t2[1]==t4[3] or t3[1]==t4[4]:
 print(t3[1])
 AppendList.append(t3[1])
if t3[2]==t4[0] or t3[2]==t4[1] or t3[2]==t4[2] or t3[2]==t4[3] or t3[2]==t4[4]:
 print(t3[2])
 AppendList.append(t3[2])
if t3[3]==t4[0] or t3[3]==t4[1] or t3[3]==t4[2] or t3[3]==t4[3] or t3[3]==t4[4]:
 print(t3[3])
 AppendList.append(t3[3])
if t3[4]==t4[0] or t3[4]==t4[1] or t3[4]==t4[2] or t3[4]==t4[3] or t3[4]==t4[4]:
 print(t3[4])
 AppendList.append(t3[4])

#Ticket 3 & 5
if t3[0]==t5[0] or t3[0]==t5[1] or t3[0]==t5[2] or t3[0]==t5[3] or t3[0]==t5[4]:
 print(t3[0])
 AppendList.append(t3[0])
if t3[1]==t5[0] or t3[1]==t5[1] or t3[1]==t5[2] or t3[1]==t5[3] or t3[1]==t5[4]:
 print(t3[1])
 AppendList.append(t3[1])
if t3[2]==t5[0] or t3[2]==t5[1] or t3[2]==t5[2] or t3[2]==t5[3] or t3[2]==t5[4]:
 print(t3[2])
 AppendList.append(t3[2])
if t3[3]==t5[0] or t3[3]==t5[1] or t3[3]==t5[2] or t3[3]==t5[3] or t3[3]==t5[4]:
 print(t3[3])
 AppendList.append(t3[3])
if t3[4]==t5[0] or t3[4]==t5[1] or t3[4]==t5[2] or t3[4]==t5[3] or t3[4]==t5[4]:
 print(t3[4])
 AppendList.append(t3[4])
 
 #Ticket 3 & 6
if t3[0]==t6[0] or t3[0]==t6[1] or t3[0]==t6[2] or t3[0]==t6[3] or t3[0]==t6[4]:
 print(t3[0])
 AppendList.append(t3[0])
if t3[1]==t6[0] or t3[1]==t6[1] or t3[1]==t6[2] or t3[1]==t6[3] or t3[1]==t6[4]:
 print(t3[1])
 AppendList.append(t3[1])
if t3[2]==t6[0] or t3[2]==t6[1] or t3[2]==t6[2] or t3[2]==t6[3] or t3[2]==t6[4]:
 print(t3[2])
 AppendList.append(t3[2])
if t3[3]==t6[0] or t3[3]==t6[1] or t3[3]==t6[2] or t3[3]==t6[3] or t3[3]==t6[4]:
 print(t3[3])
 AppendList.append(t3[3])
if t3[4]==t6[0] or t3[4]==t6[1] or t3[4]==t6[2] or t3[4]==t6[3] or t3[4]==t6[4]:
 print(t3[4])
 AppendList.append(t3[4])
 
#Ticket 3 & 7
if t3[0]==t7[0] or t3[0]==t7[1] or t3[0]==t7[2] or t3[0]==t7[3] or t3[0]==t7[4]:
 print(t3[0])
if t3[1]==t7[0] or t3[1]==t7[1] or t3[1]==t7[2] or t3[1]==t7[3] or t3[1]==t7[4]:
 print(t3[1])
if t3[2]==t7[0] or t3[2]==t7[1] or t3[2]==t7[2] or t3[2]==t7[3] or t3[2]==t7[4]:
 print(t3[2])
if t3[3]==t7[0] or t3[3]==t7[1] or t3[3]==t7[2] or t3[3]==t7[3] or t3[3]==t7[4]:
 print(t3[3])
if t3[4]==t7[0] or t3[4]==t7[1] or t3[4]==t7[2] or t3[4]==t7[3] or t3[4]==t7[4]:
 print(t3[4])
 
#Ticket 3 & 8
if t3[0]==t8[0] or t3[0]==t8[1] or t3[0]==t8[2] or t3[0]==t8[3] or t3[0]==t8[4]:
 print(t3[0])
 AppendList.append(t3[0])
if t3[1]==t8[0] or t3[1]==t8[1] or t3[1]==t8[2] or t3[1]==t8[3] or t3[1]==t8[4]:
 print(t3[1])
 AppendList.append(t3[1])
if t3[2]==t8[0] or t3[2]==t8[1] or t3[2]==t8[2] or t3[2]==t8[3] or t3[2]==t8[4]:
 print(t3[2])
 AppendList.append(t3[2])
if t3[3]==t8[0] or t3[3]==t8[1] or t3[3]==t8[2] or t3[3]==t8[3] or t3[3]==t8[4]:
 print(t3[3])
 AppendList.append(t3[3])
if t3[4]==t8[0] or t3[4]==t8[1] or t3[4]==t8[2] or t3[4]==t8[3] or t3[4]==t8[4]:
 print(t3[4])
 AppendList.append(t3[4])

#Ticket 3 & 9
if t3[0]==t9[0] or t3[0]==t9[1] or t3[0]==t9[2] or t3[0]==t9[3] or t3[0]==t9[4]:
 print(t3[0])
 AppendList.append(t3[0])
if t3[1]==t9[0] or t3[1]==t9[1] or t3[1]==t9[2] or t3[1]==t9[3] or t3[1]==t9[4]:
 print(t3[1])
 AppendList.append(t3[1])
if t3[2]==t9[0] or t3[2]==t9[1] or t3[2]==t9[2] or t3[2]==t9[3] or t3[2]==t9[4]:
 print(t3[2])
 AppendList.append(t3[2])
if t3[3]==t9[0] or t3[3]==t9[1] or t3[3]==t9[2] or t3[3]==t9[3] or t3[3]==t9[4]:
 print(t3[3])
 AppendList.append(t3[3])
if t3[4]==t9[0] or t3[4]==t9[1] or t3[4]==t9[2] or t3[4]==t9[3] or t3[4]==t9[4]:
 print(t3[4])
 AppendList.append(t3[4])

########### TICKET 4 ###################





print("\n")
print(AppendList)
print(" ")

freqt = [None] * len(AppendList) 
visited = -1
for i in range(0, len(AppendList)):    
    count = 1
    for j in range(i+1, len(AppendList)):    
        if(AppendList[i] == AppendList[j]):    
            count = count + 1
            #To avoid counting same element again   
            freqt[j] = visited
    if(freqt[i] != visited):    
        freqt[i] = count

for i in range(0, len(AppendList)):
 if(freqt[i] != visited):
  print(list(str(AppendList[i])), end=" ")
