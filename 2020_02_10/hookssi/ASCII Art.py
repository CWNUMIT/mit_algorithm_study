import sys
import math

# A ~ Z 범위 밖의 문자라면 아스키 아트로 ? 출력해야함 주의
# 출력을 한번에 해야한다는 것도 주의할 점

def print_ASCII_Art(t, l, h, ASCII):
    result = ''
    
    for y in range(0, h):
        for ch in t:
            if( ord('A') <= ord(ch) and ord(ch) <= ord('Z') ):
                index = ord(ch) - ord('A')
            else:
                index = ord('Z') - ord('A') + 1
        
            result += ''.join(ASCII[y][index * l : (index + 1) * l])
        result += '\n'

    print(result)
    
l = int(input())
h = int(input())
t = input().upper()

ASCII = list()
for i in range(h):
    row = input()
    ASCII.append(list(row))
    
print_ASCII_Art(t, l, h, ASCII)