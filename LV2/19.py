# 전화번호 목록
def solution(phone_book): 

    d = dict(zip(phone_book, [0] * len(phone_book)))
    
    for p in phone_book:
        arr = ""
        for w in p:
            arr += w
            if arr in d and arr != p:
                return False
    return True