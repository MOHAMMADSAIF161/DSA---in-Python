image=[[1,1,0],[1,0,1],[0,0,0]]
res=[]
for row in image:
    row.reverse()
    for i in range(len(row)):
        row[i]=1-row[i]
print(image)


