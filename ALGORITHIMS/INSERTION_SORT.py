nums=[89,1,3,56,7,44]
for i in range(1,len(nums)):
    a=nums[i]
    j=i-1
    while j>=0 and a<nums[j]:
        nums[j+1]=nums[j]
        j=j-1
        print(j)
    nums[j+1]=a
print(nums)
