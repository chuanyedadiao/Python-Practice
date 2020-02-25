def make_album(singer,album,songs = 5):
    infor = {singer:album,"songs":songs}
    return infor

def printdict(dict):
    for key,value in dict.items():
        print(key +" : "+str(value))


dict = make_album("Spyair","4",20)
printdict(dict)

dict = make_album("Future Islands","In evening air")
printdict(dict)

dict = make_album("Beach House","Myth")
printdict(dict)
