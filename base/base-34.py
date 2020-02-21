def fun(x):
    return x**3

n = int(input('输入n'))
sum=0
for i in range(1,n+1):
    sum+=fun(i)
print('{0}个自然数的立方和为{1}'.format(n,sum))
