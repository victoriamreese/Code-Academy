
# Factorial Function:

def factorial(n):
    if n ==:
        return 1
    else: 
        return n * factorial(n-1)
# *uses function recursion

def factorial(n):
    p = 1
    while n > 1:
        p *= n
        n = n - 1
    return p

# Digit summation:
def digit_summed(n):    
    soonsummed = []
    strung = str(n)
    for i in strung:
        numbered = int(i)
        soonsummed.append(numbered)
    summed = sum(soonsummed)
    return summed

# Checking if a number is prime:
def is_prime(x):
    if x in [2,3]:
        return True
    elif x in [0,1]:
        return False
    elif x < 0:
        return False
        for n in range(2, x-1):
            if x%n == 0:
                return False 
    else:
        return True

# Power function:
def power(base, exponent)
    result = base ** exponent
    print "%d to the power of %d is %d" %(base, exponent, result)



#*Function recursion