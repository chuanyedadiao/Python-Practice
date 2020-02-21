def JudgeNum(n):
    if n>1:
        for i in range(2,n):
            if n%i==0:
                return False
        else:
            return True
    else:
        return False


low = int(input('输入最低的范围'))
high = int(input('输入最高的范围'))
for i in range(low,high+1):
    if JudgeNum(i):
        print(i)
