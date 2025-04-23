def is_perfect(n):
    if n <= 1:
        return False
    
    divisors_sum = 0
    
    for i in range(1, n):
        if n % i == 0:
            divisors_sum += i
    
    return divisors_sum == n

number = int(input("Enter a number: "))
if is_perfect(number):
    print(f"{number} is a perfect number.")
else:
    print(f"{number} is not a perfect number.")
