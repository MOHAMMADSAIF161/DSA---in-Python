def isBadVersion(val,main):
    return val==main
p=[]
for i in range(5):
    if i<2:
        r=i+1
    else:
        r=i
    p.append(isBadVersion(i,r))
# n=['F','F','F','T','T']
def badversion(arr):
    l=0
    r=len(arr)-1
    while l<=r:
        mid=(l+r)//2
        if arr[mid]==True and (mid==0 or arr[mid-1]==False):
            return mid
        elif arr[mid]==False:
            l=mid+1
        else:
            r=mid-1
print(badversion(p))