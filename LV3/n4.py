# 정수 삼각형
def solution(triangle):
    answer = -2147000000
    L = len(triangle)
    dp = [[0] * i for i in range(1, L + 1)]
    if L == 1:
        return triangle[0][0]
    
    dp[0][0] = triangle[0][0]
    dp[1][0] = triangle[0][0] + triangle[1][0]
    dp[1][1] = triangle[0][0] + triangle[1][1]
    for i in range(2, L):
        for j in range(len(dp[i])):
            if j != 0 and j != (len(dp[i]) - 1):
                dp[i][j] = max(triangle[i][j] + dp[i - 1][j], triangle[i][j] + dp[i - 1][j - 1])
            else:
                if j == 0:
                    dp[i][j] = triangle[i][j] + dp[i - 1][0]
                else:
                    dp[i][j] = triangle[i][j] + dp[i - 1][j - 1]
            
            if answer < dp[i][j]:
                answer = dp[i][j]

    return answer