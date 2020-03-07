
def solution(A):
    var = bin(A)[2:]            #convert intiger to binary, remove first two char
    mylist = var.split("1")     # spliting elements of string to list
    mylist2 = list(dict.fromkeys(mylist)) # remove double elements from list
    mylist3 = sorted(mylist2)  # sorting list from min to max number
    mylist4 = [len(i) for i in mylist3] # counting every list element and return new list
    mylist5 = min(mylist4)
    print(mylist5)





solution(16)




