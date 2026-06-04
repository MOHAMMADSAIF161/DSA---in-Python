strs = ["eat","tea","tan","ate","nat","bat"]
d={}
for word in strs:
    key="".join(sorted(word))
    if key in d:
        d[key].append(word)
    else:
        d[key]=[word]

print(list(d.values()))
