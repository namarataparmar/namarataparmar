def olen(s):
    if len(s)==0:
        return 0
    if s[0]==' ':
        return olen(s[1:])
    else:
        return 1+olen(s[1:])
