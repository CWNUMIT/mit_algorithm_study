def remove_couple(s):
    stack = []
    for i in range(0, len(s)):
        a = s[i]
        if(len(stack) > 0):
            b = stack.pop()
            if(a != b):
                stack.append(b)
                stack.append(a)
        else:
            stack.append(a)
            
    if(len(stack) > 0):
        return False
    else:
        return True
    
def solution(s):
    answer = list(s)
    return remove_couple(answer)
    
