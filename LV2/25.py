# 무인도 여행
import sys
sys.setrecursionlimit(10 ** 6)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y, board):
    global summ
    summ += board[x][y]
    board[x][y] = 0
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < len(board) and 0 <= ny < len(board[0]) and board[nx][ny] != 0:
            dfs(nx, ny, board)
             
def solution(maps):
    answer = []
    n = len(maps)
    m = len(maps[0])
    board = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if maps[i][j] != 'X':
                board[i][j] = int(maps[i][j])         
                
    for i in range(n):
        for j in range(m):
            global summ
            summ = 0
            if board[i][j] != 0:
                dfs(i, j, board)
                answer.append(summ)
    if answer:
        answer.sort()
        return answer
    else:
        return [-1]