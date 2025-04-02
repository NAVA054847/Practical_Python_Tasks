import numpy as np
#1
a = np.array([1, 4, 5, 8,2,3,4,5,6,2], int)
b= np.array([1,3,4,5], int)
c = np.array([5,6,7,8], int)
#2
print(b*c)

#3
d=b*c
print(d.argmax())

#4
matrix = a.reshape(2, 5)
print(matrix)

#5
row_avg = np.mean(matrix, axis=1)
print(row_avg)

#6

condition = np.logical_and(a > 2, a < 8)
last_condition = np.logical_and(condition, a % 2 == 1)
print(last_condition)

#7
print(a[last_condition])

#8
print(np.where((a > 2) & (a < 8) & (a % 2 == 1), a^a,10))

#9
np.random.seed(3987)
matrix = np.random.randint(100, 201, size=(3, 7))
print(matrix)






