# 기사단원의 무기 
def solution(number, limit, power):
    result = []
    answer = 0
    
    for n in range(1, number + 1):
        cnt = 0
        for i in range(1, int(n ** (1/2)) + 1):
            if n % i == 0:
                cnt += 1
                if ((i ** 2) != n):
                    cnt += 1
        result.append(cnt)
                
    for p in result:
        if p > limit:
            answer += power
        else:
            answer += p
            
    return answer
            
