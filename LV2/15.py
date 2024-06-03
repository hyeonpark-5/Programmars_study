# 예상 대진표
def solution(n,a,b):
    answer = 0

    while n > 1:
        n //= 2
        answer += 1
        for i in range(1, n + 1):
            if 2 * (i - 1) <= a <= 2 * i:
                a = i
            if 2 * (i - 1) <= b <= 2 * i:
                b = i
        if a == b:
            break
            
    return answer
