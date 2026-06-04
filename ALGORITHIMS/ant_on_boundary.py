nums =[3,2,-3,-4]
s=0
c=0
for i in nums:
    if i>0:
        s+=i
    else:
        s-=abs(i)
    if s==0:
        c+=1

print(c)

