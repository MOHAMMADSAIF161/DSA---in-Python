def digit(p:int):
    if p>0 and p<10:
        return 1
    elif p==0:
        return 0
    sn=int(p/10)
    ans=digit(sn)
    return ans
print(digit(234))
    