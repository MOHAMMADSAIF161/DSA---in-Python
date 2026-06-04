gain = [-4,-3,-2,-1,4,3,2]
ans=[]
big=0
for i in range(len(gain)+1):
    if i==0:
        ans.append(0)
        p=0
    else:
        p=ans[i-1]+gain[i-1]
        ans.append(p)
print(big)

