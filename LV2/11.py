# 스킬트리
from collections import deque
def solution(skill, skill_trees):
    answer = len(skill_trees)
    res = 0
    for s in skill_trees:
        skills = deque(list(skill))
        for i in s:
            if i in skills:
                if i == skills[0]:
                    skills.popleft()
                else:
                    res += 1
                    break
        
        
    return answer - res