nums1=[1,3,4,8,8,9]
nums2=[2,9,8,8,8]
f={}
for i in nums1:
    if i in f:
        f[i]+=1
    else:
        f[i]=1
print(f)
p={}
for i in nums2:
    if i in p:
        p[i]+=1
    else:
        p[i]=1
print(p)
common=p.items() & f.items()
print(common)
