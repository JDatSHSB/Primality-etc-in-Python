# Name: James Dietz
# Date: 11/12/2012
# Comment: Fermat's PRP test.
import random

def test():
    print("Program to perform the Fermat PRP test in Python.")
    n = int(input("Please enter the number to test: "))
    print()
    prp = []
    composite = 0
    print("The chance of failure for the Fermat PRP test is ")
    print("1/2^-k where k is the number of iterations of the test performed. ")
    testStrength = int(input("How many iterations would you like to run?: "))
    iterations = 0
    if n % 2 == 0:
        print("{0} is composite - it is divisible by two.".format(n))
        exit
    else:
        pass
    while iterations <= testStrength:
        iterations += 1
        base = random.randrange(1,4*testStrength)
        number_to_test = base**(n-1)
        if number_to_test % n == 1:
            print("{0} is a base {1}-PRP.".format(n, base))
        else:
            composite = 1
            if len(prp) > 0:
                print(prp)
                print("These bases threw up a false positive. \n")
            else:
                print("{0} is composite.".format(n))
            break
    if iterations == testStrength and composite == 0:
        print("{0} is a PRP for bases {1}".format(n, bases))
    else:
        pass
test()
