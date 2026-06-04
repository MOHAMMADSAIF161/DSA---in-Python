num=6666
digit=[int(d) for d in str(num)]
a=[]
for i in range(len(digit)):
    if digit[i]==6:
        digit[i]=9
        p=("".join(str(d) for d in digit))
        a.append(int(p))
        digit[i]=6
    else:
        digit[i]=6
        p=("".join(str(d) for d in digit))
        a.append(int(p))
        digit[i]=9
t=(max(a))
print(type(t))