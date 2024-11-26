from collections import deque
# ord - 64
def solution(msg):
    msg += '0'
    d = {}
    w = ''
    answer = []
    i = 26
    
    for n in range(len(msg)):
        w += msg[n]
        if (len(w) > 1 and w not in d) or w == '0':
            i += 1
            if len(w[:-1]) == 1:
                answer.append(int(ord(w[:-1])) - 64)
            else:
                answer.append(d[w[:-1]])
            d[w] = i
            w = w[-1]    
    return answer