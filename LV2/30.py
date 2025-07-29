#택배상자
from collections import deque

def solution(order):
    T = len(order)
    belt = []
    idx = 0
    num = 1
    
    while T > 0:
        if num > len(order):
            if belt:
                if belt[-1] != order[idx]:
                    break
                else:
                    idx += 1
                    belt.pop()
            
            T-= 1
            continue
        
        if num != order[idx]:
            if belt and belt[-1] == order[idx]:
                idx += 1
                belt.pop()
                T-= 1
                continue
            else:
                belt.append(num)
                T += 1
        else:
            idx += 1

        num += 1
        T-= 1

    return idx

