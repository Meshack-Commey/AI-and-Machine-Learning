""" ### README.md

Title: UNSUPERVISED-LEARNING DATA ANALYSIS GENERIC PROGRAM

desc:
This project is based on Unsupervise Learning Concept, Statistics and Data Analysis
the computer system extracts or draws data set(observations) by itself to make further analysis on those data, without any supervised interferance

feat:
        The outline of Statistics as a Subject

#project structure
|
|------> Data Collection
|------> Data inspection
|------> Statistics
            |---> Diagrammatic representation of Data
                    |---> Tables
                            |---> Frequency Distributive Table
                            |---> Relative Frequency Distributive Table
                            |---> Cummulative Frequency Distributive Table
                    |
                    |---> Graphs
                            |---> Bar Chart
                            |---> Pie Chart
                            |---> Pictogram
                            |---> Histogram
                            |---> Frequency Polygon
                            |---> Cummulative Frequency Curve
                            |---> Stem-and-Leaf plot
                            |---> Box-and-Whisker plot
            |       
            |---> Summary Statistics 
                    |---> Measures of Central Tendancy
                            |---> Averages
                                    |---> Mode
                                    |---> Median
                                    |---> Mean
                                            |---> geometric mean
                                            |---> Harmonic mean
                                            |---> Quadratic mean
                                            |--->
                    |
                    |---> Measures of Despersion
                            |---> Range
                            |---> Quartile Range
                            |---> Decile
                            |---> Percentiles
                            |---> Mean Absolute Deviation
                            |---> Standard Deviation
                            |---> Variance
                            
Theory:
             |---> Tables
                     |---> Steps to Construct a Frequency Distributive Table
                             |#1:  Determine the Range
                             |#2:
                             |#3:
                             |#4:
                             |#5:
                             |#6:
                             |#7:
                     
                     
"""

import os, time, random, string, cmath#

Machinetime = time.asctime(time.localtime(time.time()))
print("\n \t \t    Configuration Settings ")
print("\t ", "------------------------------------------")
print("\t         ", Machinetime)

#Set Run Time
print("\t","-------------------------------------------")
#runtime = int(input("\t         Set Run Time (in seconds): "))
runtime = 1

#print("\n    Generating {} datasets in {} seconds, please wait... \n".format(xyKeys, total_runtime))

#Generate new data into MachineTickets.csv file
print("   ","--------------------------------------------------")
print("   "," |","Project: ","|","DATA ANALYSIS GENERIC PROGRAM")
print("   ","--------------------------------------------------")


#  DATA COLLECTION
#-----------------------------------
#Function for drawing data set
def draws():
			 available_draws = list(range(1,91)) #The Range of draws(1 <= draws <= 90)
			 Draw_Data = [ ] #Draw data
			 for draw in range(5):
			  pick_draw = random.choice(available_draws)
			  Draw_Data.append(pick_draw)
			  available_draws.remove(pick_draw)
			  #returns 5 numbers as a Draw
			 return Draw_Data
			
#xDraw class
class xDraw:
	def ticket1():
		for i in range(1):
			ticket1 = draws()
			#print(ticket1)
			time.sleep(runtime)
		return ticket1
	def ticket2():
		for i in range(1):
			ticket2 = draws()
			#print(ticket2)
			time.sleep(runtime)
		return ticket2
	def ticket3():
		for i in range(1):
			ticket3 = draws()
			#print(ticket3)
			time.sleep(runtime)
		return ticket3
	def ticket4():
		for i in range(1):
			ticket4 = draws()
			#print(ticket4)
			time.sleep(runtime)
		return ticket4
	def ticket5():
		for i in range(1):
			ticket5 = draws()
			#print(ticket5)
			time.sleep(runtime)
		return ticket5
	def ticket6():
		for i in range(1):
			ticket6 = draws()
			#print(ticket6)
			time.sleep(runtime)
		return ticket6
	def ticket7():
		for i in range(1):
			ticket7 = draws()
			#print(ticket7)
			time.sleep(runtime)
		return ticket7
	def ticket8():
		for i in range(1):
			ticket8 = draws()
			#print(ticket8)
			time.sleep(runtime)
		return ticket8
	def ticket9():
		for i in range(1):
			ticket9 = draws()
			#print(ticket9)
			time.sleep(runtime)
		return ticket9
	def ticket10():
		for i in range(1):
			ticket10 = draws()
			#print(ticket10)
			time.sleep(runtime)
		return ticket10
	def ticket11():
		for i in range(1):
			ticket11 = draws()
			#print(ticket11)
			time.sleep(runtime)
		return ticket11
	def ticket12():
		for i in range(1):
			ticket12 = draws()
			#print(ticket12)
			time.sleep(runtime)
		return ticket12
	def ticket13():
		for i in range(1):
			ticket13 = draws()
			#print(ticket13)
			time.sleep(runtime)
		return ticket13
	def ticket14():
		for i in range(1):
			ticket14 = draws()
			#print(ticket14)
			time.sleep(runtime)
		return ticket14
	def ticket15():
		for i in range(1):
			ticket15 = draws()
			#print(ticket15)
			time.sleep(runtime)
		return ticket15

#DRAWS
Draw1 = xDraw.ticket1()
print("\t \t", Draw1)
Draw2 = xDraw.ticket2()
print("\t \t", Draw2)
Draw3 = xDraw.ticket3()
print("\t \t", Draw3)
Draw4 = xDraw.ticket4()
print("\t \t", Draw4)
Draw5 = xDraw.ticket5()
print("\t \t", Draw5)
Draw6 = xDraw.ticket6()
print("\t \t", Draw6)
Draw7 = xDraw.ticket7()
print("\t \t", Draw7)
Draw8 = xDraw.ticket8()
print("\t \t", Draw8)
Draw9 = xDraw.ticket9()
print("\t \t", Draw9)
Draw10 = xDraw.ticket10()
print("\t \t", Draw10)
Draw11 = xDraw.ticket11()
print("\t \t", Draw11)
Draw12 = xDraw.ticket12()
print("\t \t", Draw12)
Draw13 = xDraw.ticket13()
print("\t \t", Draw13)
Draw14 = xDraw.ticket14()
print("\t \t", Draw14)
Draw15 = xDraw.ticket15()
print("\t \t", Draw15)

#----------------------------------------------------------------------------------------------------------------------------------------------------

# DATA INSPECTION
#-------------------------------
#Unlabeled Dataset
ms = [ Draw1, Draw2, Draw3, Draw4, Draw5, Draw6, Draw7, Draw8, Draw9, Draw10, Draw11, Draw12, Draw13, Draw14, Draw15]

Raw_Data = [
 # ball 1,  #ball 2,  #ball 3,  #ball 4,  #ball 5
ms[0][0],ms[0][1],ms[0][2],ms[0][3],ms[0][4], 
ms[1][0],ms[1][1],ms[1][2],ms[1][3],ms[1][4], 
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

#-----------------------------------------------------------------------------------------------------------------------------------------------------------
print(" ")
print("Unlabelled Dataset (Observations)")
print(Raw_Data)
print(" ")
print("Total number of observations = ", len(Raw_Data))
print(" ")
print("maximum observation = ", max(Raw_Data))
print("minimum observation = ", min(Raw_Data))


#SUMMARY STATISTICS
#--------------------------------------
#construct a frequency distribution table
#.........................................................................
#1:-------> Determine the Range
Range = max(Raw_Data) - min(Raw_Data)
print("Range = {} \n".format(Range))

#2:--------> Determine the Class (K)
# n = number of observed data points
n = len(Raw_Data)
#p = pow(2, 7)
# since (2 power 7 = 128) which is near to n = 75,
#Take Class, K = 7
klass = [ ]
for k in range(15):
 y = pow(2, k)
 if(y >= n):
  klass.append(k)
Class = min(klass) #Class
print("Class = ", Class)

#3:---------> Determine the Class Size or width, W
Class_Size = round(Range / Class)
print("Class size = ", Class_Size)

#4:---------> Determine the Lower and Upper Limit
#----------------------------------------------------------------
lower_limit = min(Raw_Data)
print("Lower Limit = ", lower_limit)
upper_limit = max(Raw_Data)
print("Upper Limit = ", upper_limit)
#----------------------------
###: using the UPPER LIMIT,
#................................
#multiples of the Class Size
values = [ ]
for i in range(1, 91):
 class_multiples = Class_Size * i
 values.append(class_multiples)
 #print(values)
#multiple closely below to the upper limit
below = [ ]
for i in range(0, 90):
  if (values[i] <= upper_limit):
   below.append(values[i])
   #print(values[i], end=" ")
print(" ")
#Value Below Upper Limit
try:
 Below_Limit = max(below)
 Lower_Class_Limit = Below_Limit
 print("Value below the Upper Limit ",upper_limit," is ", Lower_Class_Limit)
except:
 ValueError
print("\n")
#..................
#multiples closely above the lower limit
above = [ ]
for i in range(0, 90):
  if (values[i] >= upper_limit):
   above.append(values[i])
   #print(values[i], end=" ")
print(" ")
#Value Above Upper Limit
try:
 Above_Limit = min(above)
 Upper_Class_Limit = Above_Limit - 1
 print("Value above the Upper Limit ",upper_limit," is ", Above_Limit)
except:
 ValueError
print("\n")
"""----------------------------
###: using the LOWER LIMIT
#................................
#Value Below Upper Limit
try:
 Below = max(below)
 Lower_Class_Limit = Below
 print("Value below the Lower Limit ",lower_limit," is ", Below)
except:
 ValueError
print("\n")
Upper_Class_Limit = Above
lower_class_limit = Upper_Class_Limit - Class_Size
#Value Above Lower Limit
try:
 Above = min(above)
 upper_class_limit = Above - 1
 print("Value above the Lower Limit ",lower_limit," is ", Above)
except:
 ValueError
print("\n")
"""
try:
 print("\n Lower class limit = ", Lower_Class_Limit)
 print("\n Upper class limit = ", Upper_Class_Limit)
 print("\n")
except:
 ValueError

#-----------------------------------------------------------------------------------------------__-------------------------------__-------------------------
#5:--------------> CLASS & CLASS INTERVAL
print("       Class Interval: ")
print("     ------------------- \n")
Lower_Class_Limits = [ ] #Lower Class Limits Domain from the Highest Lower Class Limit to the Least Lower Class Limit
Upper_Class_Limits = [ ] #Upper Class Limits Domain form the Highest Upper Class Limit to the Least Upper Class Limit


"""
#Interval Data Ranking from Lower Class intervals to Upper Class intervals
sorted_Lower_Class = sorted(Lower_Classes)
sorted_Upper_Class = sorted(Upper_Classes)
"""
#Interval Range
for i in range(0, Class + 1):
 #Class Interval
 class_interval = " {} ".format(Lower_Class_Limit - (Class_Size * i))+" --- "+" {} ".format(Upper_Class_Limit - (Class_Size * i))
 low_class = Lower_Class_Limit - (Class_Size * i) #Lower Class Limits
 up_class = Upper_Class_Limit - (Class_Size * i) #Upper Class Limits
 if (low_class >= 0) and (up_class >= 0):
  Lower_Class_Limits.append(low_class)
  Upper_Class_Limits.append(up_class)
  print("      ", class_interval)
 
print("\n Interval Size:  ", Upper_Class_Limits[0] - Lower_Class_Limits[0]," \n ")
print("Lower Class Limit Domain: ", Lower_Class_Limits, "\n")
print("Upper Class Limit Domain: ", Upper_Class_Limits, "\n")
#print("Sorted Class Limits: ")
#print("Lower Limit Class Domain: ", sorted_Lower_Class, "\n")
#print("Upper Limit Class Domain: ", sorted_Upper_Class, "\n")

#6:----------> CLASS MARK / MIDPOINT ---->
print("\n     Class Mark: ")#They are the True Classes
print("     ---------------- \n")
Class_Mark = [ ]
for i in range(0, Class):
 midpoint = (Upper_Class_Limits[i] + Lower_Class_Limits[i]) / 2
 Class_Mark.append(midpoint)
 print("     ", midpoint, "\n")
 
print("Class Mark = ", Class_Mark)
print(" ")
#7:-----------> CLASS BOUNDARIES ---------->
print("     Class Boundaries: ") #They are the Exact or Real Limits of the Class Interval
print("    ------------------------ \n")
Lower_Boundaries = [ ]
Upper_Boundaries = [ ]
boundary = (Lower_Class_Limits[0] - Upper_Class_Limits[1]) / 2
 
for i in range(0, Class):
 lower_boundary = Lower_Class_Limits[i] - boundary
 upper_boundary = Upper_Class_Limits[i] + boundary
 Lower_Boundaries.append(lower_boundary)
 Upper_Boundaries.append(upper_boundary)
 class_boundary_interval = " {} ".format(lower_boundary)+" --- "+" {} ".format(upper_boundary)
 print("     ", class_boundary_interval)

#-----------------------------------------------------------------------------------------------__-------------------------------__-------------------------
#8:----------> FREQUENCY ----------->
#Array 'freq'' will store frequencies of element

freq = [None] * len(Raw_Data) 
visited = -1

for i in range(0, len(Raw_Data)):    
    count = 1
    for j in range(i+1, len(Raw_Data)):    
        if(Raw_Data[i] == Raw_Data[j]):    
            count = count + 1
            #To avoid counting same element again   
            freq[j] = visited
    if(freq[i] != visited):    
        freq[i] = count

#Displays the Tally of each data present in the Raw Data
print(" \n ")
print("---------------------------------------------------------------")
print("      Data Values          |       Tally of Raw Data ")
print("----------------------------------------------------------------");
Dataset = [ ] #Dataset = a collection of well-defined data which have been extracted from the Raw_Data based on their frequency
data_frequency = [ ] #Frequency of each Data value
for i in range(0, len(freq)):    
    if(freq[i] != visited):
        edata = str(Raw_Data[i])
        efreq = str(freq[i])
        Dataset.append(Raw_Data[i])
        data_frequency.append(freq[i])
        print("           " + edata+ "                 |                " + efreq)
        
print("----------------------------------------------- \n")
print("Data: ", Dataset, " \n ")
print("Frequency: ", data_frequency, " \n ")

print("Length of Data Values: ", len(Dataset))
print("Length of Frequency: ", len(data_frequency))
print(" ")


for i in range(len(Dataset)):
 for j in range(len(Upper_Class_Limits)):
  if (Dataset[i] <= Lower_Class_Limits[j] and Dataset[i] <= Upper_Class_Limits[j]):
   add = 0
   add = add + data_frequency[i]
   print(add)
 









"""
Data_Range = [ ] #the Range inwhich each Data lies
for i in range(0, Class):
 if(Lower_Class_Limits[i] >= 0) and (Upper_Class_Limits[i] >= 0):
  data_range = range(Lower_Class_Limits[i], Upper_Class_Limits[i])
  list_interval = data_range
  Data_Range.append(list_interval)
  print("Interval: ", data_range)
  #print("interval: ", list_interval)
  
print(" \n ")
print("Interval Range: ", Data_Range," \n")
print("Length of Interval Range: ", len(Data_Range))
print(" \n ", Data_Range[0], "   its length is ", len(Data_Range[0]), " \n ")


for i in range(0, len(Data_Range)):
 for j in range(0, len(Data_Range[i])):
  for k in range(0, len(Dataset)):
     if Dataset[k] == Data_Range[i][i+1]:
      Frequency = data_frequency[k]
      print("Range: ",Data_Range[j], "  Data: ", Dataset[k], " Freq: ", Frequency)
     
 """








"""
#Draws in Dataset that occurs n number of times

drawn_once = [ ]
once_freq = [ ]
def once():
						for i in range(0, len(freq)):
						 if(freq[i] == 1):
						  once = int(Dataset[i])
						  On = freq[i]
						  drawn_once.append(once)
						  once_freq.append(On)
						  print(once, end=", ")
#once()
print("\n ")

drawn_twice = [ ]
def twice():
				for i in range(0, len(freq)):
					if(freq[i] == 2):
					 twice = int(Dataset[i])
					 drawn_twice.append(twice)
					 print(twice, end=", ")
#twice()
print(" ")		

drawn_thrice = [ ]
Freq = [ ]
def thrice():
				for i in range(0, len(freq)):
					if(freq[i] == 3):
					 thrice = int(Dataset[i])
					 drawn_thrice.append(thrice)
					 print(thrice, end=", ")
#thrice()
print(" ")

drawn_four = [ ]
def four():
				for i in range(0, len(freq)):
					if(freq[i] == 4):
					 four = int(Dataset[i])
					 drawn_four.append(four)
					 print(four, end =", ")
#four()
print(" ")

drawn_five = [ ]
def five():
				for i in range(0, len(freq)):
					if(freq[i] == 5):
					 five = int(Dataset[i])
					 drawn_five.append(five)
					 print(five, end=" ")
#five()
print(" ")

drawn_six = [ ]
def six():
				for i in range(0, len(freq)):
					if(freq[i] == 6):
					 six = int(Dataset[i])
					 drawn_six.append(six)
					 print(six, end=", ")
#six()
print(" ")

drawn_seven = [ ]
def seven():
				for i in range(0, len(freq)):
					if(freq[i] == 7):
					 seven = int(Dataset[i])
					 drawn_seven.append(seven)
					 print(seven, end=", ")
#seven()
#######################################################################
print("-------------------------------------------------------")
print("Balls which occurred Once \n ")
once()
print(" \n \n ")
print("-------------------------------------------------------")
print("Balls which occurred Twice \n ")
twice()
print("\n \n")
print('-------------------------------------------------------')
print("Balls which occurred Thrice \n ")
thrice()
print("\n \n")
print("-------------------------------------------------------")
print("Balls which occurred Four times \n")
four()
print("\n \n")
print("-------------------------------------------------------")
print("Balls which occurred Five times \n ")
five()
print("\n \n")
print("-------------------------------------------------------")
print("Balls which occurred Six times \n ")
six()
print("\n \n")
print("-------------------------------------------------------")
print("Balls which occurred Seven times \n ")
seven()
print("\n \n")
print("-------------------------------------------------------")
							
print("\n")
# Tally



#Array FreQ will store frequencies of element

FreQ = [None] * len(INTERVAL_RANGE) 
visited = -1

for i in range(0, len(INTERVAL_RANGE)):    
    count = 1
    for j in range(0, len(Dataset)):    
        if(INTERVAL_RANGE[i] == Dataset[j]):    
            count = count + 1
            #To avoid counting same element again   
            FreQ[i] = visited
    if(FreQ[i] != visited):    
        FreQ[i] = count

#Displays the frequency of each Dataset present in INTERVAL_RANGE  
print(" \n ")
print("    -------------------------------------------------")
print("            Class            |         Frequency")
print("   --------------------------------------------------"); 
   
for i in range(0, len(FreQ)):    
    if(FreQ[i] != visited):
        FREQ = str(FreQ[i])
        for k in range(0, Class):
         if(Lower_Class_Limits[k] >= 0) and (Upper_Class_Limits[k] >= 0):
          for j in range(0, Class + 1):
           Class_Interval = " {} ".format(Lower_Class_Limit - (Class_Size * j))+" --- "+" {} ".format(Upper_Class_Limit - (Class_Size * j))
          print("    " + Class_Interval + "         |         " + FREQ)
         





for i in range(0, len(drawn_once)):
   for j in range(0, Class + 1):
    if(drawn_once[i] in range(Lower_Class_Limits[j], Upper_Class_Limits[j])) and (once_freq[0] is 1):
     print(drawn_once[i], "  ----->  ",Lower_Class_Limits[j], " --- ", Upper_Class_Limits[j])
 
   elif i in range(Lower_Class_Limits[1], Upper_Class_Limits[1]):
    print(i, "  ----->  ",Lower_Class_Limits[1], " --- ", Upper_Class_Limits[1])
   elif i in range(Lower_Class_Limits[2], Upper_Class_Limits[2]):
    print(i, "  ----->  ",Lower_Class_Limits[2], " --- ", Upper_Class_Limits[2])
   elif i in range(Lower_Class_Limits[3], Upper_Class_Limits[3]):
    print(i, "  ----->  ",Lower_Class_Limits[3], " --- ", Upper_Class_Limits[3])
   elif i in range(Lower_Class_Limits[4], Upper_Class_Limits[4]):
    print(i, "  ----->  ",Lower_Class_Limits[4], " --- ", Upper_Class_Limits[4])
   elif i in range(Lower_Class_Limits[5], Upper_Class_Limits[5]):
    print(i, "  ----->  ",Lower_Class_Limits[5], " --- ", Upper_Class_Limits[5])
   elif i in range(Lower_Class_Limits[6], Upper_Class_Limits[6]):
    print(i, "  ----->  ",Lower_Class_Limits[6], " --- ", Upper_Class_Limits[6])
   
 """ 
   

