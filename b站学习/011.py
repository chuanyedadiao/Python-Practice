member = ['牡丹','小布丁','黑夜','米兔','已经','福禄娃娃','竹林小溪','Crazy迷恋']
print(member)


temp = member[0]
member[0] = member[1]
member[1] = temp
print(member)

member.remove('已经')
print(member)

del member[1]
print(member)

print(member.pop())
print(member.pop(1))

print(member[:2])
print(member[0:])
print(member[1:2])

