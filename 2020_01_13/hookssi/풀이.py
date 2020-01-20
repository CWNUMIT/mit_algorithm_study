import math

def gcd(a, b):
	while(b!=0):
		r = a % b;
		a = b;
		b = r;
	return a

def GetUselessBox(w, h):
    num = 0
    나머지 = 0
    index = 0
    
    while(index < w):
        if((나머지 + h) <= w):
            몫 = math.floor((w - 나머지) / h)
            num += 몫
            index += 몫
            나머지 = (나머지 + h * 몫)
        else:
            num += 2
            index += 1
            나머지 = (나머지 + h - w)
    return num

def solution(w,h):
    최소공약수 = gcd(w, h)
    
    minW = (int)(w / 최소공약수)
    minH = (int)(h / 최소공약수)
    
    최소사각형갯수 = w / minW
    총사각형갯수 = w * h
    
    if(minW >= minH):
        못쓰는사각형갯수 = GetUselessBox(minW, minH)
    else:
        못쓰는사각형갯수 = GetUselessBox(minH, minW)
    
    answer = 총사각형갯수 - 최소사각형갯수 * 못쓰는사각형갯수

    return answer