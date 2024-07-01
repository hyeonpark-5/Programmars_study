def solution(wallpaper):
    answer = []
    result_row = []
    result_col = []
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == '#':
                result_row.append(i)
                result_col.append(j)
    
    if len(result_row) > 1 and len(result_col) > 1:
        result_row[-1] += 1
        result_col.sort()
        result_col[-1] += 1
        answer = [result_row[0], result_col[0], result_row[-1], result_col[-1]]
    else:
        answer = [result_row[0], result_col[0], result_row[-1] + 1, result_col[-1] + 1 ]
        
    
    print(answer)
    return answer