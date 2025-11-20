#대충 만든 자판
def solution(keymap, targets):
    answer = []
    dic = {}
    
    for key in keymap:
        for i in range(len(key)):
            if key[i] in dic:
                dic[key[i]] = min(i + 1, dic[key[i]])
            else:
                dic[key[i]] = i + 1
                
    for target in targets:
        count = 0
        for t in target:
            if t not in dic:
                count = - 1
                break
            
            count += dic[t]
        answer.append(count)
                                      
    return answer