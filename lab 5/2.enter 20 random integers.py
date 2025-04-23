import random
l=[]
for i in range(20):
   l.append(random.randint(1,200))

print(l)

for i in l:
   i=l.index(l[i])
   print(i)  
   i=i+1

  
