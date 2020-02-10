def solution(m, n, board):
    answer = 0
    
    mat = [[True for col in range(n)] for row in range(m)]
    
    print(mat)
    
    end = False
    
    while not end:
        end = True
        #모든 칸에 대해 칸을 왼쪽 위 칸으로 보고 4개묶음이 같은지 검사
        for x in range(m-1):
            for y in range(n-1):
                if board[x][y] != "*" and board[x][y] == board[x][y+1] and board[x][y] == board[x+1][y] and board[x][y] == board[x+1][y+1]:
                    mat[x][y] = False
                    mat[x][y+1] = False
                    mat[x+1][y] = False
                    mat[x+1][y+1] = False
                    end = False
        
        # 사라질 칸을 *로 치환
        for x in range(m):
            for y in range(n):
                if mat[x][y] == False:
                    board[x] = board[x][:y] + "*" + board[x][y+1:]
                
        if not end:
            
            # *이 앞으로 오로록 정렬
            for y in range(n):
                for a in range(m):
                    for x in range(a):
                        if board[x][y] != "*" and board[x+1][y] == "*":
                            temp = board[x][y]
                            board[x] = board[x][:y] + board[x+1][y] + board[x][y+1:]
                            board[x+1] = board[x+1][:y] + temp + board[x+1][y+1:]
            
            # 정렬된 것을 mat에 반영
            for x in range(m):
                for y in range(n):
                    if board[x][y] != "*":
                        mat[x][y] = True
                    else:
                        mat[x][y] = False
    
    #* 숫자세기                    
    for x in range(m):
        for y in range(n):
            if board[x][y] == "*":
                answer += 1
    
    return answer