dog = {'name':'yumi',
       'master':'chuanye',
       'age':'3'
       }

cat = {'name':'kele',
       'master':'laowang',
       'age':'2'}

pets = [dog,cat]

for d in pets:
    for key,value in d.items():
        print(key+" : "+value)
        
