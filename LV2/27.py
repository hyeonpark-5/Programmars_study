#모음사전
ap = ["A", "E", "I", "O", "U"]
    
def solution(word):
    answer = 0
    num = []
    summ = 0
    def dfs(x, n):
        nonlocal summ, answer
        if n == word:
            answer = summ
        if x == 5:
            return
        for i in range(5):
            num.append(n + ap[i])
            summ += 1
            dfs(x + 1, n + ap[i])
            
    dfs(0,'')
    return answer