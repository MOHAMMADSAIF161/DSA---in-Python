def even(n:int)->None:
    if n==0:
        return 0
    ans=n-1
    even(ans)
    return even(ans)+2
print(even(5))