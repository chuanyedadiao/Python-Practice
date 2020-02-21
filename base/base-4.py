import cmath
a = float(input('输入a'))
b = float(input('输入b'))
c = float(input('输入c'))

d = (b**2)-(4*a*c)

x1 = (-b-cmath.sqrt(d))/(2*a)
x2 = (-b+cmath.sqrt(d))/(2*a)

print('结果是{0}和{1}'.format(x1,x2))
