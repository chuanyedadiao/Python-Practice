def Fibo(n):
    if n <= 1:
        return n
    else:
        return (Fibo(n-1)+Fibo(n-2))

count = int(input('输入项数:'))
for i in range(count):
    print(Fibo(i),end=' ')
