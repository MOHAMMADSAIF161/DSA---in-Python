n=8
total=n*(n+1)//2
for i in range(1,(n)+1):
    left_sum= i*(i+1)//2
    right_sum=total-left_sum
    if left_sum==right_sum:
        print(f'{i} is pivot')
