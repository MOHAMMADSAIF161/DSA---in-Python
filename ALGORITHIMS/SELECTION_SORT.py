nums=[4,4,1,5,3,2,1,5,2,3]
for i in range(len(nums)-1):
    current_index=i
    for j in range(i+1,len(nums)):
        if nums[j]<nums[current_index]:
            current_index=j
    nums[i],nums[current_index]=nums[current_index],nums[i]
print(nums)
