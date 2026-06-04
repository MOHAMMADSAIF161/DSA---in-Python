haystack = "sadbutsad"
needle = "sad"
def fun(p:str,s:str):
    if s in p:
        print(p.index(s))
    else:
        return -1
(fun(haystack,needle))
            