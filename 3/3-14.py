import sys
print('命令行参数如下:')
for i in sys.argv:
   print(i)
print('\n\nPython 路径为：', sys.path, '\n')

#想使用 Python 源文件，只需在另一个源文件里执行 import 语句
