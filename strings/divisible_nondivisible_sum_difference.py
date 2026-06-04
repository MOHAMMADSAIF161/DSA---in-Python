n=10
m=3
possible=[]
not_possible=[]
for i in range(n+1):
    if i%m==0:
        possible.append(i)
    else:
        not_possible.append(i)
print(max(sum(possible),sum(not_possible))-min(sum(possible),sum(not_possible)))
