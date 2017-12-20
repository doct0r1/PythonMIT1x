testList = [1, -4, 8, -9]


def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])


def addOne(a):
    return a + 1


applyToEach(testList, addOne)

print(testList)
