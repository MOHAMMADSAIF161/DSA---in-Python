ops=["1","C"]
a=[]
for i in ops:
    if i=="C":
        a.pop()
    elif i=="D":
        a.append(2*a[-1])
    elif i=="+":
        a.append(a[-1]+a[-2])
    else:
        a.append(int(i))
print(sum(a))
