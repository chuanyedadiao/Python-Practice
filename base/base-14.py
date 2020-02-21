num = int(input("请输入一个数字:"))
sum = 1

if num<0:
    print('该数字为负数。没有阶乘。')
elif num==0:
    print('0的阶乘为1')
else:
    for i in range(1,num+1):
        sum *=i
    print("{0}的阶乘是{1}".format(num,sum))
