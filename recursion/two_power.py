def power(p:int):
    if p==1:
        return 2
    sna=p-1
    ans=2*power(p-1)
    return ans
print(power(5))