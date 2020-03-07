
def solution(A):

        list = A
        list_zeros = []
        list_ones = []

        counter1 = 0
        for i in list:
            if i == 0:
                list_zeros.append()

                continue
            elif i == 1:
                list_ones.append()

        return (list_ones, list_zeros)
print(solution([1,0,0,1,0,0,1,0,0,0,0,1]))