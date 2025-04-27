# 피로도
def solution(k, dungeons):
    answer = 1
    length = len(dungeons)
    ch = [0] * length
    
    def dfs(k, summ):
        nonlocal answer
        if answer < summ:
            answer = summ
        else:
            for i in range(length):
                if ch[i] == 0 and k >= dungeons[i][0]:
                    ch[i] = 1
                    dfs( k - dungeons[i][1], summ + 1)
                    ch[i] = 0
    dfs(k, 0)
        
    return answer