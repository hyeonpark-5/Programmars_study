# 뒤에 있는 큰 수 찾기
from collections import deque
def solution(numbers):
    answer = [-1] * len(numbers)
    ch = []
    for idx, n in enumerate(numbers):
        while ch and numbers[ch[-1]] < n:
            answer[ch.pop()] = n
        ch.append(idx)
    return answer
        