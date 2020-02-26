with open("python.txt") as file1:
    #print(file1.read())
    '''for line in file1:
        print(line)'''
    lines = file1.readlines()

for line in lines:
    print(line)

