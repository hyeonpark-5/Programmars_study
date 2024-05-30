# 캐시
from collections import deque
def solution(cacheSize, cities):
    num = deque()
    answer = 0
    
    for c in cities:
        if cacheSize == 0:
            answer = len(cities) * 5
            break
        c = c.lower()
        if c in num:
            num.remove(c)
            num.append(c)
            answer += 1
        else:
            if num and len(num) == cacheSize:
                num.popleft()
            num.append(c)
            answer += 5
    return answer