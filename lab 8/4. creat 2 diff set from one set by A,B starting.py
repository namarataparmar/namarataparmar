s={"Aasta","Aditya","Bharti","Ali","Bitu","Batuk"}
print(s)

s1={item for item in s if item.startswith('A')}
s2={item for item in s if item.startswith('B')}
s3={item for item in s if item.endswith('i')}

print(s1)
print(s2)
print(s3)
