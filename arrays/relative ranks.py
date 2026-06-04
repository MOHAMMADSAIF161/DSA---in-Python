score=[10,3,8,9,4]
n=len(score)
a=[]
for i in range(n):
    t=(max(score))
    p=score.index(t)
    score.remove(t)
    a.append(p+1)
print(a)