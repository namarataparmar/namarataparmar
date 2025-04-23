def posin(n,fac=2,fact=None):
    if fact is None:
        fact=[]
    if n<2:
        return fact
    if n%fac==0:
        fact.append(fac)
        return posin(n//fac,fac,fact)
    else:
        return posin(n,fac+1,fact)

