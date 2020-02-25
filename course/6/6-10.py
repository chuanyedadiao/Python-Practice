favorite_num = {'chuanye':[4,7],
                'xiaozhong':[7],
                'zhengqing':[1,2,3],
                'xiaocui':[8,9,1],
                'siwen':[0,9,14]}

for key,value in favorite_num.items():
    for num in value:
        print(key+" likes "+str(num))
