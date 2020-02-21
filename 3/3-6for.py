sites = ["Baidu", "Google","Runoob","Taobao"]
for site in sites:
    if site == "Runoob":
        print("菜鸟教程!")
        break
    print("循环数据 " + site)
else:
    print("没有循环数据!")
print("完成循环!")

for i in range(5):
    print(i)
print('\n\n\n')
for i in range(5,9) :
    print(i)
print('\n\n\n')
for i in range(0, 10, 3) :
    print(i)
print('\n\n\n')
for i in range(-10, -100, -30) :
    print(i)
a = ['Google', 'Baidu', 'Runoob', 'Taobao', 'QQ']
for i in range(len(a)):
    print(i, a[i])
    
#还可以使用range()函数来创建一个列表
print(list(range(5)))
