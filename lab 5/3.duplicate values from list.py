import random

random_numbers = [random.randint(1, 30) for _ in range(50)]
print("Generated List:", random_numbers)

unique_numbers = list(set(random_numbers))

print("List without duplicates:", unique_numbers)
