leftArray = []
rightArray = []

def foldPaper(n, arr):
    if(n == 0):
        return arr

    leftArray = arr.copy()
    for e in leftArray:
        if(e == 1):
            rightArray.append(0)
        else:
            rightArray.append(1)

    arr.append(0)

    while(len(rightArray) != 0):
        arr.append(rightArray.pop())

    return foldPaper(n - 1, arr)

def solution(n):
    answer = []
    foldPaper(n, answer)

    return answer