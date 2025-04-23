def compute(n):

    a=str(n)

    nn=int(a*2)
    nnn=int(a*3)
    nnnn=int(a*4)

    ans=n+nn+nnn+nnnn
    return(ans)


for i in range(4,8):
    print("compute(i)=",compute(i))
