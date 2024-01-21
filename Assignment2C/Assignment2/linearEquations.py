# Solve the system of linear equations 2x + 3y = 7 and x - y = 1 using NumPy's linear algebra functions.
import numpy
a=numpy.array([[2,3],[1,-1]])
b=numpy.array([7,1])
x=numpy.linalg.solve(a,b)
for i in x:
    print(i,end=" ")