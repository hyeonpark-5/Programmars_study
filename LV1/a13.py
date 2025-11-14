#덧칠하기
def solution(n, m, section):
    answer = 0
    res = 0
    
    for s in section:
        if s > res:
            res = s + (m - 1)
            answer += 1
            
    return answer