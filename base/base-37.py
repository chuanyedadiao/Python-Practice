list1 = [1,2,3]
print(list1)

temp = list1[0]
list1[0] = list1[len(list1)-1]
list1[len(list1)-1] = temp

print(list1)
