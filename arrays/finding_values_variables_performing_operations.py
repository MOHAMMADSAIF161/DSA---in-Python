ar=["--X","X++","++X"]
def fvpo(ar):
    op=[]
    for i in ar:
        if i=="X++"or i=="++X":
            op.append(1)
        elif i=="--X"or i=="X--":
            op.append(-1)
    return sum(op)
print(fvpo(ar))