import numpy as np
with open("matrixA.txt","w") as f:
   f.write(" 1 2 3 8\n4 5 6 7\n7 8 9 6")
with open("matrixB.txt","w") as f:
    f.write(" 9 8 7 3\n6 5 4 4\n3 2 1 5")
def matrix_operation():
    A=np.loadtxt("matrixA.txt",dtype=int) 
    B=np.loadtxt("matrixB.txt",dtype=int)
    C=A+B
    print(C)
    with open("matrixC.txt","w") as out:
        out.write(str(C))
matrix_operation()