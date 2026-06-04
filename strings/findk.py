n=430043
h=str(n)
t=(list(h))
k=0
j=1
while j<len(t):
    sub=t[k:j+1]
    print(sub)
    if int(sub)% n==0:
        print("goood")
    else:
        print("skip")
    k+=1
    j+=1
    
