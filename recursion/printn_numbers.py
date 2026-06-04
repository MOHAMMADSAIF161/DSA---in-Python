def numbers(n:int):
    if n==1:
        print(n)
        return 1
    print(n)
    numbers(n-1)
(numbers(5))