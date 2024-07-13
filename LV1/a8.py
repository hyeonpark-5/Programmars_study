from collections import deque
def solution(s):
    answer = []
    a = list(set(s))
    d = dict(zip(a, [0] * len(a)))
    
    for idx, w in enumerate(s):
        if d[w] == 0:
            answer.append(-1)
        else:
            answer.append((idx + 1) - d[w])       
        d[w] = idx + 1
    return answer