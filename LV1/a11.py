# 택배 상자 꺼내기
def solution(n, w, num):
    answer = 1
    
    while True:
        col = num % w
        
        if (col == 0):
            col = w
        num += (1 + 2 * (w - col))   
        if num > n:
            break
        answer += 1
              
    return answer