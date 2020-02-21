year = int(input('输入一个年份:'))

if (year %4 ==0) & (year %100 !=0):
    print("%d 是闰年" %year)
elif year % 400 == 0:
    print("%d 是闰年" %year)
else:
    print("%d 是平年" %year)
