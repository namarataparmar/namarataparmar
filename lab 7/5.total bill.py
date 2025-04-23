d1={'bread':25,'butter':40,'chips':20}
d2={'bread':4,'butter':2,'chips':5}

total_bill = 0

for item in d1:
    total_bill += d1[item] * d2.get(item, 0)

print(total_bill)







