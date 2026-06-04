nums=[1,2,3,1]
k=5
def fun(nums):
#     for i in range(len(nums)):
#         for j in range(i+1,len(nums)):
#             if nums[i]==nums[j] and abs(i-j)<=k:
#                 return True
#     return False
    index={}
    for ind,key in enumerate(nums):
        if key in index and ind-index[key]<k:
            return True
        index[key]=ind
    return False
print(fun(nums))



