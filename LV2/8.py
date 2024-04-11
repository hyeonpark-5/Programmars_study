# 게임 맵 최단거리
from collections import deque

def solution(maps):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    n = len(maps)
    m = len(maps[0])
    
    q = deque()
    answer = 0
    q.append((0, 0))
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                q.append((nx, ny))

    if maps[n - 1][m - 1] == 1:
        answer = -1
    else:
        answer = maps[n - 1][m - 1]
        
    return answer