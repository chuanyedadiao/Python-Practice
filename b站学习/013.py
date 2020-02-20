#元组是不能任意插入删除修改的
#元组是不可以改变的
#创建元组大部分用小括号

tuple1 = (1,2,3,4,5,6,7,8)
print(tuple1)

#访问与列表一样
print(tuple1[1])
print(tuple1[5:])
print(tuple1[:5])

#拷贝
tuple2 = tuple1[:]

#修改元素,会报错
#tuple1[1] = 3

#()表示元组？？？
temp1 = (1)
print(type(temp1))
#会发现temp1是int

temp2 = 2,3,4
print(type(temp2))

#空元组
temp3 = ()
print(type(temp3))

#如果需要的元组只有一个元素
#则需按如下操作
temp4 = 1,
print(type(temp4))

#######################
#####更新 删除#########
#######################


#原来的标签temp5被给到另外一个元组，
#原来的元组未改变
#所以原来的元组在一段时间后就会被回收
temp5 = ('小甲鱼','黑夜','米兔','小布丁')
temp5 = temp5[:2]+('已经',)+temp5[2:]
print(temp5)

#删除元组
del temp5
