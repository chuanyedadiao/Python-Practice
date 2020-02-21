n = int(input('请输入数字'))
if n>1:
    for i in range(2,n):
        if n%i==0:
            print(n,'不是质数')
            break
    else:
        print(n,"是质数")
else:
    print(n,"不是质数")
