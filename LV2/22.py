# 호텔 대실
from heapq import heappush, heappop
def solution(book_time):
    book = []
    for b in book_time:
        h, m = b[0].split(':')
        hh, mm = b[1].split(':')
        book.append((int(h) * 60 + int(m), int(hh) * 60 + int(mm)))
    book.sort() 
    ch = []
    for s, e in book:
        if ch and ch[0] <= s:
            heappop(ch)
        heappush(ch, e + 10)
    return len(ch)