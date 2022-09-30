import numpy 

a = numpy.array([[2, 18,6, 83,13], [54, 12,37,28,90], [23, 12, 78,26,54]])
print(a)

print(" ")
b = a[0][0] + a[0][1] + a[0][2] + a[0][3] + a[0][4]
print(b)

c = a.shape
print(c)
"""
print(" ")
x = numpy.arange(90)
print(x)

print(" ")
t = x.reshape(3,6, 5)
print(t)
print(" ")

"""
#convert list into ndarray
u = [4, 2, 6, 8, 9]
s = numpy.asarray(u)
print(s)


