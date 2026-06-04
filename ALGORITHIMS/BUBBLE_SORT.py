nums=[24 ,5 ,6 ,32 ,2 ,4, 222 ,4, 56 , 3344, 2111 ,55 ,7]
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i]<nums[j]:
            continue
        else:
            nums[i],nums[j]=nums[j],nums[i]

print(nums)