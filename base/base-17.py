num = int(input("请输入一个数字"))
length = len(str(num))
temp = num
sum = 0

for i in range(length):
    j = temp % 10
    temp = temp // 10
    sum += (j**length)
if(sum == num):
    print("{0}是阿姆斯特朗数".format(num))
else:
    print("{0}不是阿姆斯特朗数".format(num))
