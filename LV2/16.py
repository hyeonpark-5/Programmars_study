# 영어 끝말잇기
def solution(n, words):
    person, num = 0, 0
    ch = []
    for idx, w in enumerate(words):
        person = (idx + 1) % n
        if idx == 0:
            ch.append(w)
            continue
        
        if ch[-1][-1] != w[0] or w in ch:
            person = (idx + 1) % n
            if person == 0:
                person = n
            
            num += (idx + 1) // n
            if (idx + 1) % n != 0: 
                num += 1
            break
        ch.append(w)
        
    return [person, num]