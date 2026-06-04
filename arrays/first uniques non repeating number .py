s="loveleetcode"
f={}
for i in s:
    f[i]=f.get(i,0)+1
for i in f:
    if f[i]==1:
        break
print(s.index(i))
print(f)