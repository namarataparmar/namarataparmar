def fun(n):
    return n*n

import random
l=[]
for i in range(10):
   l.append(random.randint(-15,15))
print(l)

f1=map(fun,l)
print(list(f1))
