n=list("loveleetcode")
h=[i for i in range(len(n))]
c="e"
index=[i for i,ch in enumerate(n) if ch==c]
p=[]
def min(l:list,l2:list):
    for num in l2:
        m=abs(l[0]-num)
        for n in l:
            if abs(n-num)<m:
                m=abs(n-num)
        p.append((m))
    return p
print(min(index,h))
