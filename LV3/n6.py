# 등굣길
def solution(m, n, puddles):
    answer = -1
    check = [[0] * (m + 1) for _ in range(n + 1)]
    check[1][1] = 1

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1:
                continue
                
            if [j, i] in puddles:
                check[i][j] = 0
            else:
                check[i][j] = (check[i - 1][j] + check[i][j - 1]) % 1000000007
    

    return check[n][m]