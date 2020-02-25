people = ['chuanye','zhengqing','siwen','xiaocui','xiaozhong','xiangxiang',
          'zhouxiang','guanyu']

favorite_languages = {'chuanye':'Java',
                      'xiaozhong':'C',
                      'xiangxiang':'python',
                      'zhouxiang':'ruby',
                      'guanyu':'c++'}

for person in people:
    if person in favorite_languages.keys():
        print(person.title()+"'s favorite_language is "+favorite_languages[person].title())
    else:
        print("Dear "+person.title()+", We invite you to take out investigation.")
