
def solution(A):
    B = sorted(A)
    print(B)
    mylist = list(dict.fromkeys(B))
    print(mylist)
    value = 1

    try:
        for i in mylist:
            if i + 1 == mylist[value]:
                pass
            elif i+1 < 0 or i+1 == 0:
                print(1)
                break
            else:
                print(i + 1)
                break
            value = value + 1
    except:
        print(mylist[-1] + 1)


solution([2, 3, 4, 5, 8])

