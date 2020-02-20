import random
print('-------------我爱鱼c工作室------------')
secret = random.randint(1,10)
temp = input('不妨猜一下小于现在心里想的是那个数字：')
guess = int(temp)
while guess != secret:
    temp = input("哎呀，猜错了，请重新输入吧：")
    guess = int(temp)
    if guess == secret:
        print("卧槽，你是小甲鱼心里的蛔虫吗")
        print("猜中了耶没有奖励")
    else:
        if guess > secret:
            print("大了大了")
        else:
            print("小了小了")
print("游戏结束。不玩啦")
