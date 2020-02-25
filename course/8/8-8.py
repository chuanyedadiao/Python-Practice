def make_album(singer,album,songs = 5):
    infor = {singer:album,"songs":songs}
    return infor

def printdict(dict):
    for key,value in dict.items():
        print(key +" : "+str(value))

active = True
while active:
    singer = input("Enter the singer's name:")
    album = input("Enter the singer's album:")
    printdict(make_album(singer,album))

    infor = input("Do you want to continue to input?")

    active = True if infor == "yes" else False
