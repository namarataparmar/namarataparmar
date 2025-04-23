
import random

random_numbers = [random.randint(-100, 100) for num in range(30)]
print("Generated List:", random_numbers)

positive_numbers = [num for num in random_numbers if num > 0]
negative_numbers = [num for num in random_numbers if num < 0]

# Print the lists
print("Positive numbers:", positive_numbers)
print("Negative numbers:", negative_numbers)
