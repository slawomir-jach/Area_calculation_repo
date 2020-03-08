
global source
source = [2,7,5,3,7,4]


def solution(H):                           # Finding high number in the list
    global higestBuilding
    higestBuilding = max(H)
    findPosition = H.index(higestBuilding)
    return higestBuilding


def findHigest(number):
    higestBuilding = max(number)
    return higestBuilding


def positionDubleFind(seq, item):
    startFrom = -1
    positionList = []
    while True:
        try:
            loc = seq.index(item, startFrom+1)
        except ValueError:
            break
        else:
            positionList.append(loc)
            startFrom = loc
    return positionList


def findDuble(source):
    howManyHighist = source.count(findHigest(source))
    if howManyHighist == 1:
        return False
    else:
        if howManyHighist > 2:
            return True
    print(howManyHighist)


def firstSquereCalculate():
    if findDuble(source) == False:
        print("Jekt ok ")
        listCalculate = positionDubleFind(source, findHigest(source))
        high = listCalculate[1]
        width = listCalculate[0]
        basis = (high - width)
        squere = basis * findHigest(source)
        return squere

#solution(source)
#print(findHigest(source))
#print(findDuble(source))
print(firstSquereCalculate())
print(positionDubleFind(source, findHigest(source)))
