def solution(ladders, win):
    answer = 0
    
    player = [1, 2, 3, 4, 5, 6]
    
    for e in ladders:
        temp = player[e[0]-1]
        player[e[0]-1] = player[e[1]-1]
        player[e[1]-1] = temp
        
    answer = player[win-1]
    return answer