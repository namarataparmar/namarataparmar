tpl = (100, 200, 300, 400)

lst = list(tpl)
del(lst[2])  
tpl2= tuple(lst)

print("Modified tuple:",tpl2)
