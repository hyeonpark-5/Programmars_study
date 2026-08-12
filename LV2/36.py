# 리코쳇 로봇
from collections import deque

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]



def solution(board):
    answer = 0
    start_x = 0
    start_y = 0
    n = len(board)
    m = len(board[0])
    
    check = [[0] * m for _ in range(n)]
    q = deque([])
    
    for i in range(n):
        for j in range(m):
            if board[i][j] == "R":
                q.append((i, j))
                check[i][j] = 0
    
    while q:
        x, y = q.popleft()
        
        if board[x][y] == "G":
            return check[x][y]
        
    
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] != "D":
                xx, yy = x, y
                while True:
                    n_xx = xx + dx[i]
                    n_yy = yy + dy[i]
                    
                    if n_xx < 0 or n_xx >= n or n_yy < 0 or n_yy >= m or board[n_xx][n_yy] == "D": 
                            break
                    else:        
                        xx = n_xx
                        yy = n_yy
                
                if check[xx][yy] == 0:
                    check[xx][yy] = check[x][y] + 1
                    q.append((xx, yy))
    
    return -1