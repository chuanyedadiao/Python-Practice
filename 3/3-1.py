dict1 = {'Name': 'Runoob', 'Age': 7, 'Name': '小菜鸟'}
print ("dict['Name']: ", dict1['Name'])
#不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住


##dict2 = {['Name']: 'Runoob', 'Age': 7}
##print ("dict['Name']: ", dict2['Name'])
#键必须不可变，所以可以用数字，字符串或元组充当，而用列表就不行
