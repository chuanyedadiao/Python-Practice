current_users = ['chuanye','xiaoye','xiaochuan','xiaoxu','xiaoshun']

new_users = ['chuanye','xiaocui','XiAoYe','shuiniu','siwen']

for user in new_users:
    flag = False
    for user2 in current_users:
        if user.lower() == user2.lower():
            print(user+ ' name has already been used.')
            flag = True
            break
    if flag == False:
        print(user+ ' has not been used')
