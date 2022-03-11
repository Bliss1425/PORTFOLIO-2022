#prime numbers is a positive integer greater than 1, whose only factors are 1 and the number itself.
prime = int(input("Enter the number you want to check: "))
while prime >= 2:
    for a in range(2 , prime):
        if prime % a == 0:
            print(f"{prime} is not a prime number")
            break
    else:
            print(f"{prime} is a prime number")
    break
#break statement to remove infinte loops
print("Thank You")


#http://www.learningaboutelectronics.com/Articles/How-to-exit-a-while-loop-with-a-break-statement-in-Python.php
