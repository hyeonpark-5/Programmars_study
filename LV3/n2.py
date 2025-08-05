#네트워크
def dfs(x, n, visited, board):
    visited[x] = 1
    
    for i in board[x]:
        if not visited[i]:
            dfs(i, n, visited,board)

def solution(n, computers):
    global answer
    board = [[] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if i != j and computers[i][j] == 1:
                board[i].append(j)
                
    answer = 0
    visited = [0] * n
    for i in range(n):
        if visited[i] == 0:
            answer += 1
            dfs(i, n, visited, board)
    return answer