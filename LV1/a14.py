#달리기 경주
def solution(players, callings):
    res = {}
    for i, p in enumerate(players):
        res[p] = i
    
    for call in callings:
        n = res[call]
        res[call] = n - 1
        res[players[n - 1]] = n
        players[n - 1], players[n] = players[n], players[n - 1]
        
    return players