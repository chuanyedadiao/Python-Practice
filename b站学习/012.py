list1 = [123]
list2 = [234]
print(list1 > list2)

list1.append(456)
list2.append(123)
print(list1 > list2) #只比较一个

list3 = list1+list2
print(list3)
#+号不好，两边的数据类型必须一样，否则会报错

list4 = list1 * 3
print(list4)

print(210 in list1)
print(210 not in list1)

list5 = [123, ['小甲鱼','牡丹'],456]
print('小甲鱼' in list5)
print(list5[1][1])

print(list4.count(123)) #个数

print(list1.index(456))#返回第一个出现的位置
print(list4)
print(list4.index(123,1,4)) #返回从某个位置到某个位置 特定值第一次出现的位置

list1.reverse()
print(list1)

list6 = [4,2,5,1,9,23,32,0]
list6.sort()
print(list6)
list7 = [4,2,5,1,9,23,32,0]
list7.sort(reverse=True)
print(list7)


list8 = list7[:]
list9 = list7
print(list8)
print(list9)

list7.sort()
print(list8)
print(list9)
