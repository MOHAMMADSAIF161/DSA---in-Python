from collections import Counter
nums1=[4,1,2]
nums2=[1,3,4,2]
# d={c:v for c,v in enumerate(nums2)}
for num in nums1:
    t=nums2.index(num)
    if  nums2[t+1]==len(nums2):
        print(nums2[t+1])
    if nums2[t]>nums2[t+1]:
        print("-1")
    else:
        print(nums2[t+1])
