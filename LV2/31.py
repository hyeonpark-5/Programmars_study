#땅따먹기

def solution(land):
    row = len(land)
    # check = [0] * row
    for i in range(1, row):
        for j in range(4):
            
            land[i][j] += max(land[i - 1][:j] + land[i - 1][j+1:])
    return max(land[row - 1])
    
#     def dfs(x, summ, col):
#         nonlocal answer
#         if x == row:
#             if answer < summ:
#                 answer = summ
#             return
#         for i in range(4):
#             if i != col:
#                 # check[x] = land[x][i]
#                 # print(check)
#                 dfs(x + 1, summ + land[x][i], i)
            
#     dfs(0, 0, -1)
        
