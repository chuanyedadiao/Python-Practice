guests = ['zhengqing','wuxing','laowang']
print(guests[1]+' can\'t come to my dinner')

guests[1] = 'chuanye'

guests.insert(0,'siwen')
guests.insert(2,'xiaocui')
guests.append('shuiniu')

for guest in guests:
    print('Dear '+ guest +' would you come to enjoy the dinner with me?')
