def solution(s):
    answer = ''
    d = {'zero': '0', 'one': '1', 'two': '2', 'three': '3',
        'four': '4', 'five': '5', 'six': '6', 'seven': '7',
        'eight': '8', 'nine': '9'}
    
    check = ''
    for i in s:
        if i.isalpha():
            check += i
            if check in d:
                answer += d[check]
                check = ''
        else:
            answer += i

    return int(answer)