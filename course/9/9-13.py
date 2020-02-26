from collections import OrderedDict
favorite_languages = OrderedDict()

favorite_languages['chuanye'] = 'python'
favorite_languages["xiaozhong"] = 'C'
favorite_languages['xiangxiang'] = 'java'

for name,language in favorite_languages.items():
    print(name+" "+language)
