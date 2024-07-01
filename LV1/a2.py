from collections import deque
import copy

def solution(s):
    s = deque(s)
    answer = 0
    while len(s) > 0:
        count = 1
        if len(s) == 1:
            answer += 1
        x = s.popleft()
        
        for word in copy.deepcopy(s):
            if x == word:
                count += 1   
            else:
                count -= 1
                
            s.popleft()
            if count == 0 or (len(s) == 0 and count >= 1):
                answer += 1
                break
            
    return answer