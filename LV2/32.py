# 숫자 변환하기
def solution(x, y, n):
    MAX = 2147000000
    check = [MAX] * (y + 1)
    check[x] = 0
    
    for i in range(x, y + 1):
        if check[i] == MAX:
            continue
        
        if i + n <= y:
            check[i + n] = min(check[i + n], check[i] + 1)
        if i * 2 <= y:
            check[i * 2] = min(check[i * 2], check[i] + 1)
        if i * 3 <= y:
            check[i * 3] = min(check[i * 3], check[i] + 1)
                 
    if check[y] == MAX:
        return -1
    return check[y]