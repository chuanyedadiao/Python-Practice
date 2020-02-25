people1 = {'first_name':'kawago',
          'last_name':'xu',
          'age':'21',
          'city':'ChangSha'}
people2 = {'father':'none',
           'mother':'zhengqing',
           'siblings':'none'}
people3 = {'boyfriend':'none',
           'best-friend':'shijie',
           'want to work':'ChangSha'}

people = [people1,people2,people3]

for dict in people:
    for key,value in dict.items():
        print(key+" : "+value)
