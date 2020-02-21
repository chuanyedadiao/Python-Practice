def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    return x/y

print('选择要进行的操作：\n'\
      '1.相加\n'\
      '2.相减\n'\
      '3.相乘\n'\
      '4.相除'\
      )
choice = int(input('请输入你的选择:'))

num1 = int(input('输入第一个操作数:'))
num2 = int(input('输入第二个操作数:'))

if choice == 1:
    print(num1,'+',num2,'=',add(num1,num2))
elif choice == 2:
    print(num1,'-',num2,'=',sub(num1,num2))
elif choice == 3:
    print(num1,'*',num2,'=',mul(num1,num2))
elif choice == 4:
    print(num1,'/',num2,'=',div(num1,num2))
else:
    print('错误输入')
