username = ['chuanye','xiaozhong','zhouxiang','xiaocui','admin']

if username:
    for user in username:
        if user == 'admin':
            print('Hello admin,would you like to see a status report?')
        else :
            print('Hello '+user+' ,thank you for logging in again')
else:
    print('We need to find some users')
