#주차 요금 계산
import math
def solution(fees, records):
    answer = []
    ch = {}
    for r in records:
        time, number, check = r.split()
        h, m = time.split(':')
        h, m = int(h), int(m)
        if number not in ch:
            ch[number] = [h, m, check, 0]
        else:
            if ch[number][2] == 'OUT' and check == 'IN':
                ch[number][0] = h
                ch[number][1] = m
                ch[number][2] = check
                continue
            nh = h - ch[number][0]
            nm = m - ch[number][1]
            if nm < 0:
                nh -= 1
                nm = 60 - abs(nm)
            ch[number][0] = h
            ch[number][1] = m
            ch[number][2] = check
            ch[number][3] += (nh * 60) + nm
        
    
    key = sorted(ch)
    for k in key:
        if ch[k][2] == "IN":
            nh = 23 - ch[k][0]
            nm = 59 - ch[k][1]
            if nm < 0:
                nh -= 1
                nm = 60 - abs(nm)
            ch[k][0] = h
            ch[k][1] = m
            ch[k][2] = check
            ch[k][3] += (nh * 60) + nm
            
        if ch[k][3] <= fees[0]:
            answer.append(fees[1])
        else:
            answer.append(fees[1] + (math.ceil((ch[k][3] - fees[0]) / fees[2])) * fees[3])
    return answer