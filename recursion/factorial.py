def fact(p:int):
    if p==1:
        return 1
    s=fact(p-1)
    ans =p*s
    return ans
print(fact(5))
