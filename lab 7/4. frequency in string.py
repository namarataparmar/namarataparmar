str = input("Enter a string: ")
frequency = {}

for char in str:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

print(frequency)
