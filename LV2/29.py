# 두 큐 합 같게 만들기
from collections import deque

def solution(queue1, queue2):
    
    L = len(queue1) * 4
    q1 = deque(queue1)
    q2 = deque(queue2)
    
    sum_q1 = sum(q1)
    sum_q2 = sum(q2)
    total = (sum_q1 + sum_q2) // 2
    cnt = 0
    
    while True:
        if cnt > L:
            cnt = -1
            break
            
        if sum_q1 == sum_q2:
            break
            
        if sum_q1 > sum_q2:
            n = q1.popleft()
            q2.append(n)
            sum_q1 -= n
            sum_q2 += n      
        else:
            n = q2.popleft()
            q1.append(n)
            sum_q1 += n
            sum_q2 -= n
        
        cnt += 1
        
    return cnt

