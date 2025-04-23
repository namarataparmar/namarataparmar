tpl = (1, 2, 3, 4)

lst= list(tpl)
lst[2] = 99  # Modify the third element
tpl2 = tuple(lst)

print("Modified tuple:", tpl2)
