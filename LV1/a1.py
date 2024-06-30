# 공원 산책
def solution(park, routes):
    plans = {"N":(-1,0), "S":(1,0), "W":(0,-1), "E":(0,1)}
    x, y = 0, 0
    answer = []
    for i in range(len(park)):
        for j in range(len(park[i])):
            if park[i][j] == 'S':
                x = i
                y = j
                break
    
    for i in range(len(routes)):
        plan, num = routes[i].split(' ')
        x_ = x
        y_ = y
      
        for j in range(int(num)):
            nx = x + plans[plan][0]
            ny = y + plans[plan][1]
        
            if 0 <= nx < len(park[0]) and 0 <= ny < len(park[0]) and (park[nx][ny] != 'X'):
                x = nx
                y = ny
            else:
                x = x_
                y = y_
                break
            
    answer.append(x)
    answer.append(y)
    
    return answer