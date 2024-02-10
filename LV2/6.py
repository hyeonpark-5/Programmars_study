from collections import deque
def solution(progresses, speeds):
    answer = deque([])
    ch = 0
    maxx = 0
    for i in range(len(progresses)):
        num = (100 - progresses[i]) // speeds[i]
        if (100 - progresses[i]) % speeds[i] != 0:
            num += 1
        progresses[i] = num
    
    while len(progresses) > 0:
        a = progresses.pop()
        ch += 1
        if len(progresses) == 0:
            answer.appendleft(ch)
        else:
            if a > max(progresses) and progresses[-1] < a:
                answer.appendleft(ch)
                ch = 0
            else:
                continue
                
    
    return list(answer)