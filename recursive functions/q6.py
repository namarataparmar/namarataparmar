def sanneg(l,c=0):
    if c!=len(l):
        if l[c]<0:
            l[c]=0
        else:
            return l
        return sanneg(l,c=c+1)
