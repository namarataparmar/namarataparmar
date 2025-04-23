lst = [(), ("apple", 5), (), ("banana", 2)]

l1 = [ele for ele in lst if ele ]
print(l1)

lst = [(), ("apple", 5), (), ("banana", 2)]
for i in lst :
      if (len(i)==0):
         lst.remove(i)
         print(lst)
        
       

      




