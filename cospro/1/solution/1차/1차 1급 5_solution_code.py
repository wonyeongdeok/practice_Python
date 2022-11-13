def in_range(i, j, n):
    return 0 <= i and i < n and 0 <= j and j < n

def solution(n):
    pane = [[0 for j in range(n)] for i in range(n)]
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]
    ci, cj = 0, 0
    num = 1
    while in_range(ci, cj, n) and pane[ci][cj] == 0:
        for k in range(4):
            if not in_range(ci, cj, n) or pane[ci][cj] != 0:
                break
            while True:
                pane[ci][cj] = num
                num += 1
                ni = ci + dy[k]
                nj = cj + dx[k]
                if not in_range(ni, nj, n) or pane[ni][nj] != 0:
                    ci += dy[(k + 1) % 4]
                    cj += dx[(k + 1) % 4]
                    break
                ci = ni
                cj = nj

    ans = 0
    for i in range(n):
        ans += pane[i][i]
    return ans
