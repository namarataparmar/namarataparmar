def po(a,b):
    if b==0:
        return 1
    else:
        return a*po(a,b-1)
