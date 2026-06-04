# s="abccccdd"
# t=([s.count(i) for i in set(s)])
# t.sort(reverse=True)
# ans=0
# for i in t:
#     if i&1==0:
#         ans+=i
#     else:
#         ans+=i
#         break
# print(ans)
from collections import Counter
arr=[1,2,3,4,1,2,2,3,3,4,1,2,3,4,4,5,5,5,5,6,6,7,7,4,3,3,2]
dici=Counter(arr)
# for i in range(len(arr)):
#     if arr[i] not in dici:
#         dici[arr[i]]=1
#     else:
#         dici[arr[i]]+=1


print(dici.items())