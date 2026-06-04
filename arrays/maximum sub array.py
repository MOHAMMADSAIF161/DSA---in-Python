nums=[1,12,-5,-6,50,3]
k=4
window=sum(nums[0:k])
max_ans=(window)
l=0
r=k
while r<len(nums):
    window=window-nums[l]+nums[r]
    max_ans=max(max_ans,window)
    l+=1
    r+=1
print((max_ans)/k)