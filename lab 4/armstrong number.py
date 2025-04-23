def is_armstrong(number):
    
    num_str = str(number)
    num_digits = len(num_str)
    
    
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
    
    if sum_of_powers == number:
        return True
    else:
        return False


number = 153 
if is_armstrong(number):
    print(f"{number} is an Armstrong number!")
else:
    print(f"{number} is not an Armstrong number.")
