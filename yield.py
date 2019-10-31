def myRange(a, b):
    i = a

    while (i < b):
        print('sending ' + str(i))
        yield i
        i = i + 1


def a():
    return list(myRange(1, 4))


for i in a():
    print(i)
