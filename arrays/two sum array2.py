l=0
nums=[-4,-1,0,1,2]
nums.sort()
r=len(nums)-1
while l<r:
    current=nums[l]+nums[r]
    if current==0:
        print([l+1,r+1])
        break
    elif current<0:
        l+=1
    else:
        r-=1
