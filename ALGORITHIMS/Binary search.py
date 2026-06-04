nums=[1,3,5,6]
tar= 9
def binaray(arr,val):
    l=0
    r=len(arr)-1
    while l<=r:
        mid=(l+r)//2
        if arr[mid]==val:
            return mid
        elif arr[mid] < val:
            l=mid+1
        else:
            r=mid-1
    arr.insert(l,val)
    return arr.index(val)
print(binaray(nums,tar))
    