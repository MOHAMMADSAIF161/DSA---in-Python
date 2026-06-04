a=["saif","sana"]
x="a"
# ans=[]
# for i in range(len(a)):
#     if x in a[i]:
#         ans.append(i)
# print(ans)
print([i for i,a in enumerate(a) if x in a])