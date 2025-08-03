# 서버 증설 횟수
def solution(players, m, k):
    answer = 0
    server = [0] * 24
    for i in range(24):
        if players[i] < m:
            continue
        if players[i] >= m:
            p = players[i] // m
            if server[i]:
                if server[i] < p:
                    p = p - server[i]
                else:
                    p = 0
            answer += p
            for j in range(0, k):
                if (i + j) == 24:
                    break
                server[i + j] += p
    return answer