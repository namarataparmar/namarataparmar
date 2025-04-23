# Sample dictionary of employees with their dept_no, roll_no, and salary
employees = {
    'emp1': {'dept_no': 101, 'roll_no': 1, 'salary': 5000},
    'emp2': {'dept_no': 102, 'roll_no': 2, 'salary': 6000},
    'emp3': {'dept_no': 101, 'roll_no': 3, 'salary': 7000},
    'emp4': {'dept_no': 103, 'roll_no': 4, 'salary': 4500},
    'emp5': {'dept_no': 102, 'roll_no': 5, 'salary': 8000},
}

# Create a dictionary to store min and max salaries by department
dept_salaries = {}

# Iterate through the employees dictionary and calculate min and max salary for each department
for emp, data in employees.items():
    dept = data['dept_no']
    salary = data['salary']
    
    if dept not in dept_salaries:
        dept_salaries[dept] = {'min_salary': salary, 'max_salary': salary}
    else:
        dept_salaries[dept]['min_salary'] = min(dept_salaries[dept]['min_salary'], salary)
        dept_salaries[dept]['max_salary'] = max(dept_salaries[dept]['max_salary'], salary)

print(dept_salaries)
