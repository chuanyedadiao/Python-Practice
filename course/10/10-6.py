active = True
while active:
    infor = input("Please enter the number1:")
    try:
        count1 = int(infor)
    except ValueError:
        print(infor +" is not a number.Please put in a number")
    else:
        active = False
active = True
while active:
    infor = input("Please enter the number2:")
    try:
        count2 = int(infor)
    except ValueError:
        print(infor +" is not a number.Please put in a number")
    else:
        active = False

print(count1+count2)
