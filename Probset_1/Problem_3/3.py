import numpy as np
with open("matrixA.txt","w") as f:
   f.write(" 1 2 3\n4 5 6\n7 8 9 ")
with open("matrixB.txt","w") as f:
    f.write(" 9 8 7\n6 5 4\n3 2 1")
def matrix_operation():
    A=np.loadtxt("matrixA.txt",dtype=int) 
    B=np.loadtxt("matrixB.txt",dtype=int)
    C=np.dot(A,B)
    print(C)
    with open("matrixC.txt","w") as out:
        out.write(str(C))
matrix_operation()