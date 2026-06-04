nums=[2,0,2,4,3,1,1,0]
for i in range(1,len(nums)):
    k=nums[i]
    j=i-1
    if nums[k]<nums[j]:
        nums[k]=nums[j-1]
    j+=1
print(nums)

