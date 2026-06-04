s="iloveleetcode"
words=["i","love","leetcode","apples"]
count=0
p=""
for i in words:
    if len(p)<=len(s):
        p+=i
    if p in s:
        count+=len(p)
    else:
        break
print(count==len(p))
print(count)