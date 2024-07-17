def solution(answers):
    answer = []
    
    p1 = [1, 2, 3, 4, 5] 
    p2 = [2, 1, 2, 3, 2, 4, 2, 5] 
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] 
    
    if len(answers) > 5:
        w = len(answers) // 5
        p1 *= (w + 1)
        p2 *= (w + 1)
        p3 *= (w + 1)
        
    sum1 = 0
    sum2 = 0
    sum3 = 0
    d = {1: 0, 2: 0, 3: 0}
    for i in range(len(answers)):
        if answers[i] == p1[i]:
            d[1] += 1
        if answers[i] == p2[i]:
            d[2] += 1
        if answers[i] == p3[i]:
            d[3] += 1

    for key, value in d.items():
        if value == max(d.values()):
            answer.append(key)
    
    return answer
        