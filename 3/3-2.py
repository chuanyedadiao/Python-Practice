#集合（set）是一个无序的不重复元素序列。
#可以使用大括号 { } 或者 set() 函数创建集合，
#注意：创建一个空集合必须用 set() 而不是 { }，
#因为 { } 是用来创建一个空字典。

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)
#Set（集合）有去重功能

# 下面展示两个集合间的运算.
a = set('abracadabra')
b = set('alacazam')
print(a)
print(b)
print(a-b)
print(a|b)
print(a&b)
print(a^b)

c = {x for x in 'abracadabra' if x not in 'abc'}
print(c)

#添加
thisset = set(("Google", "Runoob", "Taobao"))
thisset.add("Facebook")
print(thisset)
#还有一个方法，也可以添加元素，且参数可以是列表，元组，字典等
thisset2 = set(("Google", "Runoob", "Taobao"))
thisset2.update({1,3})
print(thisset2)
thisset2.update([1,4],[5,6])
print(thisset2)

#移除
thisset3 = set(("Google", "Runoob", "Taobao"))
thisset3.remove("Taobao")
print(thisset3)
#thisset3.remove("Facebook")   # 不存在会发生错误
#此外还有一个方法也是移除集合中的元素，且如果元素不存在，不会发生错误
thisset4 = set(("Google", "Runoob", "Taobao"))
thisset4.discard("Facebook")# 不存在不会发生错误
print(thisset4)
#可以设置随机删除集合中的一个元素
thisset5 = set(("Google", "Runoob", "Taobao", "Facebook"))
x = thisset5.pop()
print(x)

#计算集合元素个数
thisset6 = set(("Google", "Runoob", "Taobao"))
print(len(thisset6))

#清空集合
thisset6.clear()
print(thisset6)

#判断元素是否在集合中存在
thisset7 = set(("Google", "Runoob", "Taobao"))
print("Runoob" in thisset7)
print("Facebook" in thisset7)
