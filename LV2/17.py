#뉴스 클러스터링
from collections import Counter
def solution(str1, str2):
    s1 = []
    s2 = []
    for i in range(1, len(str1)):
        w = str1[i - 1] + str1[i]
        if w.isalpha():
            s1.append(w.lower())
            
    for i in range(1, len(str2)):
        w = str2[i - 1] + str2[i]
        if w.isalpha():
            s2.append(w.lower())
    
    if len(s1) == 0 and len(s2) == 0:
        return 65536

    s1 = Counter(s1)
    s2 = Counter(s2)
    
    result1 = list((s1 & s2).elements())
    result2 = list((s1 | s2).elements())
    
    return int(len(result1) / len(result2) * 65536)