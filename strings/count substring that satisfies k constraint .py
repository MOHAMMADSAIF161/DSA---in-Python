p=list('11111')
k=1
u=0
for i in range(len(p)):
    for j in range(i+1,len(p)+1):
        if p[i:j].count('0')<=k or p[i:j].count('1')<=k:
            u+=1
print(u)