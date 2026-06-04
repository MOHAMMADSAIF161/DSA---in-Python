nums=[6,5,1,2,3,4]
p=[]
for num in nums:
    if num%2==0:
        p.insert(0,num)
    else:
        p.append(num)
print(p)