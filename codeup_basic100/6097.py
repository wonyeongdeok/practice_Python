# 격자 만들기
w, h = map(int, input().split())
lattice_board = [[0 for _ in range(h)] for _ in range(w)]

# 놓을 수 있는 막대의 개수 입력
n = int(input())

# n 회 입력하여 격자판에 상태 출력
for _ in range(n):
    l, d, x, y = map(int, input().split())
    x, y = x-1, y-1
    for i in range(l):
        if d == 0:
            lattice_board[x][y+i] = 1
        elif d == 1:
            lattice_board[x+i][y] = 1

# 정답 출력 모양으로 바꾸기
for row in lattice_board:
    row = list(map(str, row))
    print(' '.join(row))
