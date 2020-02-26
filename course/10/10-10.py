with open("book.txt") as book:
    result = book.read()
print("the:" + str(result.count('the')))
