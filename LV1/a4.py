def solution(name, yearning, photo):
    answer = []
    for i in range(len(photo)):
        sum = 0
        for j in range(len(photo[i])):
            if photo[i][j] in name:
                idx = name.index(photo[i][j])
                sum += yearning[idx]
        answer.append(sum)            
    return answer