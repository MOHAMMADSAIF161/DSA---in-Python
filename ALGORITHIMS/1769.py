nums=[1,1,0]
ans=[]
for i in range(len(nums)):
    m=0
    for j in range(len(nums)):
        if nums[j]==1:
            m+=(abs(i-j))
    ans.append(m)
print(ans)
