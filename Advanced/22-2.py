import pymysql

#连接数据库

mydb = pymysql.connect(
  host="localhost",       # 数据库主机地址
  user="root",    # 数据库用户名
  passwd="shuaibi990719"   # 数据库密码
)
 
print(mydb)

#创建数据库
'''
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="123456"
)
 
mycursor = mydb.cursor()
 
mycursor.execute("CREATE DATABASE runoob_db")
'''
#输出所有数据库的列表
'''
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="123456"
)
 
mycursor = mydb.cursor()
 
mycursor.execute("SHOW DATABASES")
 
for x in mycursor:
  print(x)
'''

#创建数据表
'''
 
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="123456",
  database="runoob_db"
)
mycursor = mydb.cursor()
 
mycursor.execute("CREATE TABLE sites (name VARCHAR(255), url VARCHAR(255))")
'''
