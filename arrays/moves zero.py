num=[0,1,0,3,12]
l,r=0,0
while(r<len(num)):
    if num[r]!=0:
        num[l],num[r]=num[r],num[l]
        l+=1
    r+=1
print(num)
