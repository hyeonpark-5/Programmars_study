# 야근 지수
import heapq

def solution(n, works):
    q = []
    answer = 0

    for w in works:
        heapq.heappush(q, -w)
        
    for i in range(n):
        if not q:
            break
        num = heapq.heappop(q) * -1
        if num > 0:
            heapq.heappush(q, -(num - 1))
    
    for j in q:
        answer += (j * (-1)) ** 2
    return answer