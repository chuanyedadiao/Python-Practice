def show_magicians(magicians):
    for magician in magicians:
        print(magician)

def make_great(magicians):
    for i in range(len(magicians)):
        magicians[i] = "The Great "+ magicians[i]
    return magicians

magicians = ["chuanye","zhengqing","xiaozhong"]
magicians2 = make_great(magicians[:])
show_magicians(magicians)
print("\n\n")
show_magicians(magicians2)
