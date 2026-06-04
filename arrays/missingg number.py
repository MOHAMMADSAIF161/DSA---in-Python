nums=[9,6,4,2,3,5,7,0,1]
# for i in range(len(nums)+1):
#     if i in nums:
#         continue
#     else:
#         print(i)
#         break


# t=([i for i in range(len(nums)+1) if i not in nums])
# print(t[0])

s=sum(nums)
print(s)
t=(sum(range(len(nums)+1)))
print(t-s)