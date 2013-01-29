# Carmichael number algorithm using trial division
# Found using Korselt's criterion

class Fermat:
    import random

    def test(number):
        print("Fermat's PRP test.")
        n = int(input("Please enter a number: "))
        for c in range(1, round(n**0.5)1):
            if n % c == 0:
                # Check if c-1 divides n - 1
                p = c - 1
                m = n - 1
                if p % m == 0:
                    print(n, "is a Carmichael number.")
                    quit()
                else:
                    pass
            else:
                continue

        print()
        prp = []
        composite = 0
        print("The chance of failure for the Fermat PRP test is\n 2^-k, where k is the number of iterations performed. ")
        testStrength = int(input("How many iterations would you like to run?: "))
        iterations = 0
        if n % 2 == 0:
            print("{0} is composite - it is divisible by two.".format(n))
            quit()
        else:
            pass

        # Main testing loop
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
    
