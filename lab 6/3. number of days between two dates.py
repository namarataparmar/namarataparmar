from datetime import date

date1 = (1, 2, 2020)  # (day, month, year)
date2 = (16, 2, 2025)

obj1 = date(date1[2], date1[1], date1[0])
obj2 = date(date2[2], date2[1], date2[0])

difference = (obj2 -obj1).days

print("Number of days between the two dates:", difference)
