# 3 x n 타일링
def solution(n):
    if n % 2 != 0:
        return 0
    
    check = 0
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[2] = 3
    for i in range(4, n + 1, 2):
        check = (check + dp[i - 4]) % 1000000007
        
        dp[i] = (3 * dp[i - 2] + check * 2) % 1000000007
               
    return dp[n]