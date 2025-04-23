def is_palindrome(number):
    num_str = str(number)
    
    if num_str == num_str[::-1]:
        return True
    else:
        return False

number = 111
if is_palindrome(number):
    print("number is a palindrome!")
else:
    print("number is not a palindrome.")
