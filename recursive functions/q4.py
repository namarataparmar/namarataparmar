def revl(l):
    if l==[]:
        return None
    return l[-1]+revl[l[:-1]]

