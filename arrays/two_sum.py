arr=list(map(int,input("enter the array numbers ").split()))
target=int(input())
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]+arr[j]==target:
            l=[arr[i],arr[j]]
            print(l)
    