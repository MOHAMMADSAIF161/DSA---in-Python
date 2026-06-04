nums=[1,4,4]
k=4
def fun(n:list,target:int):
    p=[]
    for i in range(len(nums)):
        if target==nums[i]:
            return(1)
        else:
            for j in range(i+1,len(nums)):
                if sum(nums[i:j+1])>=target:
                    t=(len(nums[i:j+1]))
                    p.append(t)
    if p:
        return min(p)
    return 0
(print(fun(nums,k)))
            

        

