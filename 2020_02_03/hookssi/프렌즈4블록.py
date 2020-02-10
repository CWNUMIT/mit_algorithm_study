# 1. 블록 위치 업데이트 + 블록 삭제 및 카운트
# 2. 오른쪽 대각선 블록 확인
# 3. 오른쪽, 아래 블록 확인

def update_block(n, board):
    result = 0
    count = 0
    
    for x in range(0, n - 1):
        for y in range(0, len(board[x]) - 1):
            if(len(board[x + 1]) >= (len(board[x]) - y)):
                check_valid(x, y, board)

    for x in range(0, n):
        count += len(list(filter(lambda x: x[1], board[x])))
        board[x] = list(filter(lambda x: not x[1], board[x]))
    result += count
    
    if(count > 0):
        return result + update_block(n, board)
    return result
        
def check_valid(x, y, board):
    block = board[x][y][0]
    
    correction_pos = len(board[x+1]) - len(board[x])
    
    if(board[x + 1][y + correction_pos + 1][0] == block and board[x][y + 1][0] == block and board[x + 1][y + correction_pos][0] == block):
        board[x + 1][y + correction_pos + 1][1] = True
        board[x][y + 1][1] = True
        board[x + 1][y + correction_pos][1] = True
        board[x][y][1] = True

def Init(m, n, board):
    newBoard = list()
    
    for x in range(0, n):
        newBoard.append(list( [board[y][x],False] for y in range(0, m) ))
    return newBoard

def solution(m, n, board):
    print(m, n)
    board = Init(m, n, board)
    
    answer = update_block(n, board)
    return answer