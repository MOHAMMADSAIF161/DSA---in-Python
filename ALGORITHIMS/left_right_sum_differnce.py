nums=[10,4,8,3]
total=sum(nums)
left=0
a=[]
for i in range(len(nums)):
    right=total-left-nums[i]
    a.append(abs(left-right))
    left+=nums[i]
print(a)
