def show_magicians(magicians):
    for magician in magicians:
        print(magician)

def make_great(magicians):
    for i in range(len(magicians)):
        magicians[i] = "The Great "+ magicians[i]

magicians = ["chuanye","zhengqing","xiaozhong"]
make_great(magicians)
show_magicians(magicians)

