n=int(input("entrer n: "))
def fibo(n: int, a=1) -> int:
    if n<=1:
        return n + a
    else:
        return fibo(n-1) + fibo(n-2)

a=[]
for i in range(n):
      a.append(fibo(i))
print(a)