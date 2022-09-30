#########################
# Working with file open, write, read, close
"""
fileopen = open("msdata.csv", "w+")
fileopen.writelines( )
fileopen.close()

fileopen = open("msdata.csv", "r")
y = fileopen.readlines()
print(y)
fileopen.close()
"""
#########################
#Working with dictionary
#d = { machineKey : my_ticket }
"""d = {1 : [12,34, 87, 59, 60]}

print(d)
print(d.keys())
print(d.values())
print(d[1][0:5])
print(len(d[1]))

print(" ")"""
#########################
#working with table arrays - Matrix
"""K1 = [1,2,3,4,5]
K2 = [6,7,8,9,1]
K3 = [2,3,4,5,6]"""
"""
import numpy as np
x = np.random.random((5,5))

print("Original Array:")
print(x) 
xmin, xmax = x.min(), x.max()
print("Minimum and Maximum Values:")
print(xmin, xmax)


import numpy as np
x = np.zeros((5,5))
print("Original array:")
print(x)
print("Row values ranging from 0 to 4.")
x += np.arange(5)
print(x)
"""
#A = np.array([])
	
##############################
#Initialize array    
arr = [11, 32, 18, 33, 82, 72, 32, 5, 1];     

#Array fr will store frequencies of element    

fr = [None] * len(arr);    

visited = -1;    

     

for i in range(0, len(arr)):    

    count = 1;    

    for j in range(i+1, len(arr)):    

        if(arr[i] == arr[j]):    

            count = count + 1;    

            #To avoid counting same element again    

            fr[j] = visited;    

                

    if(fr[i] != visited):    

        fr[i] = count;    

     

#Displays the frequency of each element present in array    

print("---------------------");    

print(" Element | Frequency");    

print("---------------------");    

for i in range(0, len(fr)):    

    if(fr[i] != visited):    

        print("    " + str(arr[i]) + "    |    " + str(fr[i]));    

print("---------------------");    





