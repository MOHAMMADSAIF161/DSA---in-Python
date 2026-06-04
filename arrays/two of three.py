nums1=[1,3,2]
nums2=[2,3]
nums3=[1,2]
# t=(set(nums1).intersection(set(nums2)))
# i=(set(nums1).intersection(set(nums3)))
# j=(set(nums3).intersection(set(nums2)))
# print([(i.union(t)).union(j)])
print(set(nums1)&set(nums2)| set(nums1)&set(nums3)|set(nums2)&set(nums3))
