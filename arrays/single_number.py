arr=list(map(int,input("enter arra elements: ").split()))
def bit(arr):
    result=0
    for i in arr:
        result ^=i
    return result
print(bit(arr))