nums=[1,1,1]
p=(list(set(nums)))
o=[]
if len(p)==2:
    print(max(p))
else:
    for i in range(3):
        print(p)
        t=max(p)
        o.append(t)
        p.remove(t)
        print(p)
    print(o[len(o)-1])