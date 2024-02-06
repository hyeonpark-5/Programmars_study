# 연속 부분 수열 합의 개수
from collections import deque

def solution(elements):
    elements = deque(elements)
    n = len(elements)
    result = set()
    answer = [0] * n
    for j in range(n):
        for i in range(n):
            answer[i] += elements[i]
            result.add(answer[i])
        elements.rotate(-1)
    return len(result)