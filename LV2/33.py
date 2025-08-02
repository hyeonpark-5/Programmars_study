#마법의 엘리베이터
def solution(storey):
    answer = 0
    while(storey):
        n = storey % 10
        if n > 5:
            answer += (10 - n)
            storey += 10
        elif n < 5:
            answer += n
        else:
            if (storey // 10) % 10 > 4:
                storey += 10
            answer += 5
        storey //= 10
    
    return answer