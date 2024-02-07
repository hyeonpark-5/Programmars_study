from collections import deque
def solution(s):
    answer = -1
    s = deque(list(s))
    count  = 0
    ch = []
    for x in range(len(s)):
        for i in s:
            if i == ')' or i == ']' or i == '}':
                if len(ch) == 0:
                    count -= 1
                    break
                elif i == ')' and ch[-1] == '(':
                    ch.pop()
                elif i == ']' and ch[-1] == '[':
                    ch.pop()
                elif i == '}' and ch[-1] == '{':
                    ch.pop()
                else:
                    break
            else:
                ch.append(i)
        
        if len(ch) == 0:
            count += 1

            
        s.rotate(-1)