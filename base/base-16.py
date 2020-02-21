n = int(input('请输入需要第几项'))
a,b=0,1
if n<0:
    print('请输入正数，该数字不合法')
for i in range(n):
    print(a,end=' ')
    t = b
    b = a+b
    a = t
