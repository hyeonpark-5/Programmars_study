# 할인 행사
def solution(want, number, discount):
    result = 0
    s = 0
    ch = []
    d = dict(zip(want, number))
    
    for i in range(len(discount) - 9):
        dic = d.copy()
        for w in discount[i:i + 10]:
            if w in dic.keys():
                if dic[w] != 0:
                    dic[w] -= 1
        if sum(dic.values()) == 0:
            result += 1
    
    return result 