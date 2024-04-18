# 숫자의 표현
def solution(n):
    answer = 0
     
    for i in range(1, n + 1):
        res = 0
        for j in range(i, n + 1):
            res += j
            if res > n:
                break
            if res == n:
                answer += 1
                break
            
    return answer