nums = [-6,2,5,-2,-7,-1,3]
nums.sort()
target=-2
t=0
l=0
r=len(nums)-1
while l<r:
    if nums[l]+nums[r]<target:
        t+=(r-l)
        l+=1
    else:
        r-=1

print(t)