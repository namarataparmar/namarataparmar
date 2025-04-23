import math

def is_prime(n):
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    
    return True

number = int(input("Enter a number: "))
if is_prime(number):
    print("number is a prime number.")
else:
    print("number is not a prime number.")
