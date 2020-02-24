guests = ['zhengqing','wuxing','laowang']
print(guests[1]+' can\'t come to my dinner')

guests[1] = 'chuanye'

for guest in guests:
    print('Dear '+ guest +' would you come to enjoy the dinner with me?')

print('I invited '+str(len(guests))+' to my dinner')
