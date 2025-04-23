names_list = [("John", "Doe"), ("Jane", "Smith"), "Alice", ("Paul", "Walker"), "Emma"]

boys_count = 0
girls_count = 0

for ele in names_list:
    if isinstance(ele, tuple):
        boys_count += 1
    else:
        girls_count += 1

print("Number of boys:", boys_count)
print("Number of girls:", girls_count)
