words =["abba","baba","bbaa","cd","cd"]
#abba -> bbaa,aabb,baba,abab.....
# result=["abba","cd"]
d={}
prev_key="".join(sorted(words[0]))
d[prev_key]=words[0]
for i in range(1,len(words)):
    cur_key="".join(sorted(words[i]))
    if cur_key !=prev_key:
        
