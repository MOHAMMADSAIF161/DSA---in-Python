arr=[1,2,34,3,4,5,7,23,12]
def fun(arr):
    # count=0
    # for i in arr:
    #     if i%2!=0:
    #         count+=1
    #         if count==3:
    #             break
    #     else:
    #         count=0
    # return count == 3
    for i in range(len(arr)-2):

        if arr[i]%2!=0 and arr[i+1]%2!=0 and arr[i+2]%2!=0:
            return True
    return False

print(fun(arr))