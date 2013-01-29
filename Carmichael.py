# Carmichael number algorithm using trial division
# Found using Korselt's criterion

def carmichael():
    n = int(input("Please enter a number: "))
    for c in range(1, round(n**0.5)+1):
        if n % c == 0:
            # Check if c-1 divides n - 1
            p = c - 1
            m = n - 1
            if p % m == 0:
                print(n, "is a Carmichael number.")
            else:
                pass
        else:
            continue
carmichael()
