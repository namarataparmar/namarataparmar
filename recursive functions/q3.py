def vowghn(st):
    if len(st)==0:
        return 0
    elif st[0] in ['a','e','i','o','u','A','E','I','O','U']:
        return 1+st[1:]
