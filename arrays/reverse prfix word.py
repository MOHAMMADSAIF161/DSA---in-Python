word=("abcdef")
s="g"
if s in list(word):
    i=0
    t=(word.index(s))
    while i<t:
        word[i],word[t]=word[t],word[i]
        t-=1
        i+=1

print("".join(word))
