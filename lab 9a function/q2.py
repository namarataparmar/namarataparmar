#f= lambda lst1,lst2:lst1+lst2

lst1=[1,2,3,4,5,6]
lst2=[6,5,4,3,2,1]

f1=map(lambda lst1,lst2:lst1+lst2,lst1,lst2)
print(list(f1))
