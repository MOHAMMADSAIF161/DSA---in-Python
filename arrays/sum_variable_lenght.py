nums=[3,1,1,2]
total=0
for i in range(len(nums)):
    start=max(0,i-nums[i])
    r=nums[start:i+1]
    p=sum(r)
    total+=p
print(total)
