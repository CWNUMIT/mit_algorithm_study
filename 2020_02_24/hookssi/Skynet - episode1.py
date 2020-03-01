import sys
import math

linkInfo = dict()
gatewayInfo = list()

n, l, e = [int(i) for i in input().split()]
for i in range(l):
    # n1: N1 and N2 defines a link between these nodes
    n1, n2 = [int(j) for j in input().split()]
    
    if n1 in linkInfo:
        linkInfo[n1].append(n2)
    else:
        linkInfo[n1] = [n2]
        
    if n2 in linkInfo:
        linkInfo[n2].append(n1)
    else:
        linkInfo[n2] = [n1]
    
for i in range(e):
    ei = int(input())  # the index of a gateway node
    gatewayInfo.append(ei)

def get_link_to_sever(si):
    link = linkInfo[si]
    
    for e in link:
        if(e in gatewayInfo):
            return e, si
    for e in link:
        return get_link_to_sever(e)

# game loop
while True:
    si = int(input())  # The index of the node on which the Skynet agent is positioned this turn
    result = get_link_to_sever(si)
    print(result[1], result[0])