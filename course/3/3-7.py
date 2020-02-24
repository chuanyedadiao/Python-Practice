guests = ['zhengqing','wuxing','laowang']
print(guests[1]+' can\'t come to my dinner')

guests[1] = 'chuanye'

guests.insert(0,'siwen')
guests.insert(2,'xiaocui')
guests.append('shuiniu')


print('Sorry ,The place is full of people.I can only invite two guests with me')

while len(guests)>2:
    miss_guest = guests.pop()
    print(miss_guest+", sorry,Because of the resteraunt,I can\'t have dinner with you, even if I\'d love to enjoy this with your guys...")
for guest in guests:
    print('Dear '+ guest +' would you come to enjoy the dinner with me?')

del guests[0]
del guests[0]

print(guests)
