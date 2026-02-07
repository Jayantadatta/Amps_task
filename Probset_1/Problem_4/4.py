import numpy as np
with open("matrix.txt","w") as f:
   f.write("1 2 3\n4 5 6\n7 8 9 ")
def matrix_stuffs():
   A = np.loadtxt("matrix.txt")
   with open("answers.txt","w") as out:

    trans=A.T
    print("1. ",trans,"\n")
    out.write("1. "+"\n"+ str(trans)+"\n\n")

    trace=np.trace(A)
    print("2. ", int(trace))
    out.write("2. "+ str(int(trace)))


    if(np.array_equal(A,trans)):
      print("3. Symmetric matrix")
      out.write("3. Symmetric matrix")
    elif(np.array_equal(A,-trans)):
      print("3. Skew-symmetric matrix")
      out.write("3. Skew-ymmetric matrix")
    else:
      print("3. None of them")
      out.write("\n\n"+ "3. None of them")

    d=np.linalg.det(A)
    if(d==0):
       print("4. Non-invertible")
       out.write("\n\n"+"4. Non-invertible")
    else:
       print("4. Invertible")
   
matrix_stuffs()