l1=[1,55,7,99,7]
l2=[2,56,8,66]
print(l1,l2)
l1.insert(3,l2)
print(l1)

#sort
l=[2,55,6,9]
l.sort()
print(l)

#flattern
lnew=[[1,2],[3,4]]
for ele in l:
    if (type(ele)=="list"):
      l.extend(ele)
    else:
        lnew.append(ele)
print(lnew)
