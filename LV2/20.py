# 주식가격
from collections import deque
def solution(prices):
    answer = []
    prices = deque(prices)
    
    while prices:
        result = 0
        a = prices.popleft()
        for p in prices:
            result += 1
            if p < a:
                break
        answer.append(result)
            
        
    
    return answer