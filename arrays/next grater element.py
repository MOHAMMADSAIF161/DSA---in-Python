nums1 = [2,4]
nums2 = [1,2,3,4]
a=[]
# for i in nums1:
#     t=nums2.index(i)
#     found = False                 # flag to track if we found a greater element
#     for j in range(t+1,len(nums2)):   # start from t+1
#         if nums2[j]>i:
#             a.append(nums2[j])
#             found = True
#             break
#     if not found:
#         a.append(-1)
# print(a)
for i in nums1:
    t=nums2.index(i)                 # flag to track if we found a greater element
    for j in range(t+1,len(nums2)):   # start from t+1
        if nums2[j]>i:
            a.append(nums2[j])
            break
    else:
        a.append(-1)
print(a)
