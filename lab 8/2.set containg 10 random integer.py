import random
s={random.randint(15,46) for num in range(11)}
print(s)

a={num for num in s if num<30}
print(a)

b={num for num in s if num>35}
print(b)

print (s^b)

#check why always 10 random integer not come,and also about deletation

