arr=[1,1,0,1,1,1]
def max_repation(arr):
    count=0
    counter1=[]
    for i in range(len(arr)):
        if arr[i]==1:
            count +=1
        else:
            counter1.append(count)
            count=0
    if count>0:
        counter1.append(count)
    return max(counter1)
print(max_repation(arr))
