def exec_code(): 
    LOC = """ 
def factorial(num): 
    fact=1 
    for i in range(1,num+1): 
        fact = fact*i 
    return fact 
print(factorial(5)) 
"""
    exec(LOC) 
 
exec_code()

###Python 将字符串作为代码执行


###字符串翻转
str='Runoob'
print(str[::-1])
str='Runoob'
print(''.join(reversed(str)))
