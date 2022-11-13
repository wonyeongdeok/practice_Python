def solution(height):
    count = 0
    dx = [ -1, 1, 0, 0 ]
    dy = [ 0, 0, -1, 1 ]
    for i in range(4):
        for j in range(4):
            is_danger = True
            for k in range(4):
                if 0 <= i+dx[k] and i+dx[k] < 4 and 0 <= j+dy[k] and j+dy[k] < 4:
                    if height[i+dx[k]][j+dy[k]] <= height[i][j]:
                        is_danger = False
            if is_danger:
                count += 1
    return count