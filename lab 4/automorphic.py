def is_automorphic(number):
    square = number ** 2
    
    number_str = str(number)
    square_str = str(square)
    
    if square_str.endswith(number_str):
        return True
    else:
        return False

number = 6 
if is_automorphic(number):
    print("number is an Automorphic number!")
else:
    print("number is not an Automorphic number.")
