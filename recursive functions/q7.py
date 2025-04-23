def av(l,c=0):
    if l==[]:
        return 0
    else:
        return (l[c]+av(l,c=c+1))//len(l)

n=[1,2,3,4]    
av(n)
