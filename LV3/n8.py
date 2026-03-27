#여행경로
from collections import deque 

# def dfs(x, L, used, tickets, result):
#     global answer
    
#     if x == L - 1:
#         print(result)
#         return
        
#     for i in range(L):
#         if used[i] == 0:
#             if tickets[i][0] == result[-1]:
#                 used[i] = 1
#                 result.append(tickets[i][1])    
#                 dfs(x + 1, L, used, tickets, result)
#                 used[i] = 0
#                 result.pop()


def solution(tickets):     
    answer = []
    tickets.sort()
    L = len(tickets)
    
    def dfs(x, L, used, tickets, result):
        nonlocal answer
    
        if x == L - 1:
            answer.append(result[:])
            return
        
        for i in range(L):
            if used[i] == 0:
                if tickets[i][0] == result[-1]:
                    used[i] = 1
                    result.append(tickets[i][1])    
                    dfs(x + 1, L, used, tickets, result)
                    used[i] = 0
                    result.pop()
    
    for i in range(L):
        result = ["ICN"]
        used = [0] * L
        if tickets[i][0] == "ICN":
            result.append(tickets[i][1])
            used[i] = 1
            dfs(0, L, used, tickets, result)

    return answer[0]