# 유연근무제
def solution(schedules, timelogs, startday):
    answer = 0
    n = len(schedules)
    for i in range(n):
        h = schedules[i] // 100
        m = schedules[i] % 100
        m += 10
        if m >= 60:
            m %= 60
            h += 1
        if h > 12:
            h %= 12
        schedules[i] = h * 100 + m
        
    for i in range(n):
        check = 0
        for j in range(7):
            day = 1 + (((startday - 1) + j) % 7)
            if (day == 6 or day == 7):
                continue
            
            if timelogs[i][j] <= schedules[i]:
                check += 1
        if check == 5:
            answer += 1
            
    return answer