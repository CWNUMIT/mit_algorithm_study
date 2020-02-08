# 1. 블록 위치 업데이트 + 블록 삭제 및 카운트
# 2. 오른쪽 대각선 블록 확인
# 3. 오른쪽, 아래 블록 확인

# 옆으로 생각해서 스택형식으로 만드는 것도...

def update_block(m, n, board):
    for y in range(0, m - 1):
        for x in range(0, n - 1):
            check_valid(x, y, board)
    
    for y in range(0, m):
        for x in range(0, n):
            if(board[y][x][1]):
                board[y][x][0] = 0
    
    print(board)
def check_valid(x, y, board):
    block = board[y][x][0]
    
    if(board[y + 1][x + 1][0] == block and board[y][x + 1][0] == block and board[y + 1][x][0] == block):
        board[y + 1][x + 1][1] = True
        board[y][x + 1][1] = True
        board[y + 1][x][1] = True
        board[y][x][1] = True

def Init(m, n, board):
    for y in range(0, m):
        for x in range(0, n):
            board[y] = list(board[y])
            board[y][x] = [board[y][x], False]

def solution(m, n, board):
    Init(m, n, board)
    update_block(m, n, board)
    
    answer = 0
    return answer