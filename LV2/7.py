#프로세스
from collections import deque

def solution(priorities, location):
    answer = 0
    new_priorities = deque([])
        
    for idx, p in enumerate(priorities):
        new_priorities.append((idx, p))
        
    priorities.sort()
  
    while new_priorities:        
        num = new_priorities.popleft()
        
        if num[1] == priorities[-1] :
            answer += 1
            priorities.pop()
           
            if num[0] == location:
                break     
        else:
            new_priorities.append(num)

    return answer