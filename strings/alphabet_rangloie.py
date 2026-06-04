s=3
chars=[chr(i) for i in range(97,123)]
chars=chars[:s]
index=list(range(s))
index=index+index[-2::-1]
for i in index:
    start_index=i+1
    original=(chars[-start_index:])
    reverse=original[::-1]
    row=reverse+original[1::]
    row=(" ".join(row))
    width=4*s-3
    row=(row.center(width,'-'))
    print(row)