import math

def nCr(n, r):
    return math.comb(n, r)

def nPr(n, r):
    return math.perm(n, r)

n = 5
r = 3

print(f"{n}C{r} = {nCr(n, r)}")   
print(f"{n}P{r} = {nPr(n, r)}")  
