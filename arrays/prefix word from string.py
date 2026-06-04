n="hellohello hellohello"
pt=(n.split())
s="he"
def fun(s,pt):
    for i in pt:
        if i.startswith(s):
            print(pt.index(i))
           
    return -1
print(fun(s,pt))