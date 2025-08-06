# 단어변환

def res(w1, w2):
    cnt = 0
    for i in range(len(w1)):
        if w1[i] != w2[i]:
            cnt += 1  
    if cnt > 1:
        return 0
    return 1
            
def dfs(x, c, target,words, check):
    global answer
    if x == target:
        if c < answer:
            answer = c
        return
    
    for i in range(len(words)):
        if check[i] == 0 and res(x, words[i]) == 1:
            check[i] = 1
            dfs(words[i], c + 1,target, words, check)
            check[i] = 0
        
def solution(begin, target, words):
    global answer
    answer = 2147000000
    check = [0] * len(words)
    
    if target not in words:
        return 0
    
    dfs(begin, 0, target, words, check)
    
    return answer