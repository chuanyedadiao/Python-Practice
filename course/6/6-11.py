cities = {'Xian':{'country':'China',
                  'population':'48million',
                  'fact':'where buried the first lord of China'},
          'San Francisco':{'country':'America',
                           'population':'12million',
                           'fact':'RICHHHHHHHHH'},
          'Tokyo':{'country':'Japan',
                   'population':'19million',
                   'fact':'There are a lot of different culture'}
          }

for city,infor in cities.items():
    print("\n"+city+" : ")
    for key,value in infor.items():
        print(key+" : "+value)
        
