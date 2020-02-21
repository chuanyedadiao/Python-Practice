'''
30 个人在一条船上，超载，需要 15 人下船。

于是人们排成一队，排队的位置即为他们的编号。

报数，从 1 开始，数到 9 的人下船。

如此循环，直到船上仅剩 15 人为止，问都有哪些编号的人下船了呢？
'''
left={}
for x in range(1,31):
    left[x] = 1

stayShip = 1
offShip = 0
count=0

while stayShip<=31:
    if stayShip == 31:
        stayShip = 1
    elif offShip == 15:
        break
    else:
        if left[stayShip] == 0:
            stayShip+=1
            continue
        else:
            count+=1
            if count == 9:
                offShip+=1
                left[stayShip]=0
                count=0
                print('{0} get off the ship'.format(stayShip))
            else:
                stayShip+=1
                continue
