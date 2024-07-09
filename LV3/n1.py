import heapq
def solution(operations): 
    answer = []
    for w in operations:
        if w == 'D 1':
            if answer:
                answer.sort()
                answer.pop()
            else:
                continue
        elif w == 'D -1':
            if answer:
                heapq.heappop(answer)
            else:
                continue
        else:
            i, num = w.split()
            heapq.heappush(answer,int(num))
    answer.sort()
    if answer:
        return [answer[-1], answer[0]]
    else:
        return [0, 0]
