num=[1,2,3,4,5,6,1]
ans=[]
s=0
for i in range(len(num)):
    if i ==0:
        prf=num[i]
        ans.append(prf)
    else:
        s=prf+num[i]
        ans.append(s)
        prf=s
# print(ans[len(ans)-1])
l=0
r=3
i=0
count=0
final=[]
while (r<len(num)):
    if count==0:
        final.append( (ans[len(ans)-1])  -  (ans[r]) )
    else:
        final.append((ans[len(ans)-1])  -  (ans[r]) + ans[i])
        i+=1
    count+=1
    r+=1
    l+=1
    
print(final)

