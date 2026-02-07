with open("array_input.txt","w") as f:
    f.write("1 2 3 4 5\n")
    f.write("10 20 30 40 50")
def sum_of_arrays():
    try:
        with open("array_input.txt","r") as f:
            lines=f.readlines()
            arr1= list(map(int,lines[0].split()))
            arr2= list(map(int,lines[1].split()))
            results=[a+b for a,b in zip(arr1,arr2)]
            print("Sum of the arrays: ",results)
            with open("array_output.text","w") as out:
                out.write(str(results))
    except FileNotFoundError:
        print("File is not found")
sum_of_arrays()    