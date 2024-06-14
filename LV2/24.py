#오픈채팅방
def solution(record):
    answer = []
    ch = {}
    result = []
    for r in record: 
        a = r.split()
        if a[0] != 'Change':
            result.append((a[0], a[1]))
        if a[1] not in ch:
            ch[a[1]] = a[2]
        else:
            if a[0] == "Enter" and ch[a[1]] != a[2]:
                ch[a[1]] = a[2]
        if a[0] == 'Change':
            ch[a[1]] = a[2]
    
    for word, user in result:
        if word == 'Enter':
            answer.append(ch[user] + '님이 들어왔습니다.')
        else:
            answer.append(ch[user] + '님이 나갔습니다.')
    return answer