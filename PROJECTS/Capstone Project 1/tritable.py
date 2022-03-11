print("\t\tNumber Pyramid")
#Input function-User can enter any number
num = int(input("Enter a positive number: "))
print("\n")
#range()returns an immutable sequence of numbers between the given start integer to the stop integer
#num rows&colums - The range of integers ends at stop - 1
for a in range(1, num+1 ):
    for b in range(1, a+1 ):
          print(a * b,end = " ")
    print("\n ")
