def solution(n):
    answer = [0]
    
    for i in range(n-1):
        temp = []
        temp = answer[:]
        temp.reverse()
        
        for j in range(0, len(temp)):
            if temp[j] == 1:
                temp[j] = 0
            else :
                temp[j] = 1
        
        answer.append(0)
        answer.extend(temp)
    
    return answer