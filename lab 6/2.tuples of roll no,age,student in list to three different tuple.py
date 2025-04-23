students = [(101, "namarata", 20), (102, "nirali", 22), (103, "siddharth", 21)]

roll_no = []
names = []
ages = []

for student in students:
    roll_no.append(student[0])
    names.append(student[1])
    ages.append(student[2])

print("Roll No:", roll_no)
print("Names:", names)
print("Ages:", ages)
