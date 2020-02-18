### Python 

1. keyword 关键字

   ```python
   'False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield'
   ```

2. Python中单行注释以 **#** 开头

3. 用缩进来表示代码块，不需要{}。*缩进的空格数是可变的，但是同一个代码块的语句必须包含相同的缩进空格数*

   ```python
   if True:
       print ("True")
   else:
       print ("False")
   ```

   上述正确

   ```python
   if True:
       print ("Answer")
       print ("True")
   else:
       print ("Answer")
     print ("False")    # 缩进不一致，会导致运行错误
   ```

4. 多行语句使用\

   ```python
   total = item_one + \
           item_two + \
           item_three
   ```

   在 [], {}, 或 () 中的多行语句，不需要使用反斜杠(\)

   ```python
   total = ['item_one', 'item_two', 'item_three',
           'item_four', 'item_five']
   ```

5. number类型 `int` `bool` `float` `complex`

6. 字符串String

   * 单引号和双引号使用完全相同
   * 三引号('''或""")可以指定一个多行字符串
   * 转义符 '\'
   * 反斜杠可以用来转义，使用r可以让反斜杠不发生转义。。 如 r"this is a line with \n" 则\n会显示，并不是换行。
   * 按字面意义级联字符串
   * 字符串可以用 + 运算符连接在一起，用 * 运算符重复。
   * Python 中的字符串有两种索引方式，从左往右以 0 开始，从右往左以 -1 开始。
   * 字符串不能改变
   * 没有单独的字符类型，一个字符就是长度为 1 的字符串。
   * 截取的语法格式如下：变量[头下标:尾下标:步长]

   ```python
   word = '字符串'
   sentence = "这是一个句子。"
   paragraph = """这是一个段落，
   可以由多行组成"""
   ```

   

7. 

