def solution(pos):
    dx = [1,1,-1,-1,2,2,-2,-2]
    dy = [2,-2,-2,2,1,-1,-1,1]
    cx = ord(pos[0]) - ord("A")
    cy = ord(pos[1]) - ord("0") - 1
    ans = 0
    for i in range(8):
        nx = cx + dx[i]
        ny = cy + dy[i]
        if nx >= 0 and nx < 8 and ny >= 0 and ny < 8:
            ans += 1
    return ans