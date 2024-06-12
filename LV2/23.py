#파일명 정렬
def solution(files):
    answer = []
    ch = []
    for f in files:
        head, number, tail = '', '', ''
        idx = 0
        for w in f:
            if w.isdigit() == True:
                break
            head += w
            idx += 1
        for w in range(idx, len(f)):
            if f[w].isdigit() == False:
                break
            number += f[w]
            idx += 1  
        tail = f[idx:]
        ch.append((head.lower(), int(number), tail, number, head)) 
    
    ch.sort(key=lambda x:(x[0], x[1]))
    
    for c in ch:
        answer.append(c[4] + c[3] + c[2])

    return answer