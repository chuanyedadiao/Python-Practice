a = float(input('输入边长a'))
b = float(input('输入边长b'))
c = float(input('输入边长c'))

s = (a+b+c) / 2

area = (s*(s-a)*(s-b)*(s-c))**0.5
print('三角形的面积是%0.2f' %area)
