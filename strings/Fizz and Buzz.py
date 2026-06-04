n=15
print([ "FizzBuzz" if i%3 and i%5==0 else"Fizz" if i%3==0 else "Buzzz" if i%5==0 else  f"{i}" for i in range(1,n+1) ])
