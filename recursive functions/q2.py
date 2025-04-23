def bina(n):
    if n==0:
        return '0'
    if n==1:
        return '1'
    
    else:
        return bina(n//2)+str(n%2)
