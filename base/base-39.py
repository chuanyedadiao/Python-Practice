List = [10, 11, 12, 13, 14, 15]
List.reverse()
print(List)

def countX(lst, x):
    return lst.count(x)
 
lst = [8, 6, 8, 10, 8, 20, 10, 8, 8]
x = 8
print(countX(lst, x))

list1 = [10, 20, 1, 45, 99]
 
print("最小元素为:", min(list1))

list1 = [10, 20, 1, 45, 99]
 
print("最大元素为:", max(list1))

def check(string, sub_str): 
    if (string.find(sub_str) == -1): 
        print("不存在！") 
    else: 
        print("存在！") 
 
string = "www.runoob.com"
sub_str ="runoob"
check(string, sub_str)
