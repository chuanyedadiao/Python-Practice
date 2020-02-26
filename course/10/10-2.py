with open("python.txt") as file1:
    lines = file1.readlines()

for i in range(len(lines)):
    lines[i] = lines[i].replace("python","C")
    print(lines[i])
