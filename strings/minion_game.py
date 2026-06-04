str="BANANA"
s1=0
s2=0
for i in range(len(str)):
    if str[i] in 'AEIOU':
        s1+=len(str[i:])
    else:
        s2+=len(str[i:])
print(s1,s2)
if s1>s2:
    print("kevin",s1)
else:
    print("saurth",s2)


