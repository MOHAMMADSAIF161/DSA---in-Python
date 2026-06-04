nums = [0,1,2,2,3,0,4,2]
l=0
val=2
c=0
while l<len(nums):
    if nums[l]==val:
        nums.pop(l)
    else:
        l+=1
        c+=1
print(nums)
print(c)
 