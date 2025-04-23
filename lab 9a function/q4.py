lst=["madam","python","malayalam",12321]
f1=filter(lambda s :str(s)==str(s)[::-1],lst)
print(list(f1))
