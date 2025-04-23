def fun():
    print("fun")

def disp():
    print("display")

def msg():
    print("message")

lst=[fun,disp,msg]#assing any fun to var

for f in lst:
    f()
    
