num=1248
c=0
for d in set(str(num)):
    if int(d)//num==0 or 1:
        c+=1
print(c)
