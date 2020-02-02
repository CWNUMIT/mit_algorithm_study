import math

def solution(a,b):
    
    g = math.gcd(a,b)
    
    w = a/g
    h = b/g
    
    answer = a*b
    
    count = 1
    
    i = 0
    j = 0
    
    xacc = 0
    yacc = 0
    
    while i < w - 1 or j < h - 1:
        xacc += w
        yacc += h

        if xacc/yacc == 1:
            i += 1
            j += 1
            xacc = 0
            yacc = 0
                       
        elif xacc/yacc > 1:
            i += 1
            xacc -= w
            
        else:
            j += 1
            yacc -= h

        count += 1

    return answer-(count*g)