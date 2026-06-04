nums=[10,6,2,10,2,7,9,5]
nums.sort()
for i in nums:
    d=set()
    l=0
    r=len(nums)-1
    while l<r:
        t=(nums[l]+nums[r])/2
        l+=1
        r-=1
        d.add(t)
print(len(d))