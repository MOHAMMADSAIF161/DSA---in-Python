nums=[-1,0,1,2,-1,-4]
d=([])
def fun(nums):
    for i in range(len(nums)-2):
        arr=sorted(nums[i+1:])
        l=0
        r=len(arr)-1
        while l<r:
            total=nums[i]+arr[l]+arr[r]
            if total==0:
                (d.append([nums[i],arr[l],arr[r]]))
                l+=1
                r-=1
            elif nums[i]+arr[l]+arr[r]<=0:
                l+=1
            else:
                r-=1
    t=[sorted(x) for x in d]
    return [list(x) for x in set(tuple(x)for x in t)]

print(fun(nums))