def count_alphabets_and_digits(s):
    alphabets = 0
    digits = 0
    
    for char in s:
        if char.isalpha():
            alphabets += 1
        elif char.isdigit():
            digits += 1
            
    return alphabets, digits

input_string = input("Enter a string: ")
alphabets, digits = count_alphabets_and_digits(input_string)
print(f"Number of alphabets: {alphabets}")
print(f"Number of digits: {digits}")
