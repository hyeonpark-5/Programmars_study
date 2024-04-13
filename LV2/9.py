# 다음 큰 숫자
def solution(n):
    num = bin(n)[2:]
    n_ = num.count('1')
    word = n + 1
    answer = 0
    while True:
        b = bin(word)[2:]
        b_ = b.count('1')
        if n_ == b_:
            answer = word
            break
        
        word += 1
    
    return answer