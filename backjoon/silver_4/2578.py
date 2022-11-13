import itertools
import sys

n = 5
# 철수 빙고판 만들기
board = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    nums = list(map(int, input().split()))
    for j in range(n):
        board[i][j] = nums[j]

# 사회자가 부를 때마다 빙고판에서 숫자 지우기
cnt = 0
for _ in range(n):
    nums = list(map(int, input().split()))
    for num in nums:
        bingo = 0
        for i, j in itertools.product(range(n), range(n)):
            # 사회자가 부르는 숫자를 빙고판에서 0으로 변경
            if board[i][j] == num:
                cnt += 1
                board[i][j] = 0
                # 우하향 대각선 빙고일 경우
                if board[0][0] + board[1][1] + board[2][2] + board[3][3] + board[4][4] == 0:
                    bingo += 1
                # 우상향 대각선 빙고일 경우
                if board[4][0] + board[3][1] + board[2][2] + board[1][3] + board[0][4] == 0:
                    bingo += 1
                # 가로줄 빙고일 경우
                for row in board:
                    if sum(row) == 0:
                        bingo += 1

                # 세로줄 빙고일 경우
                rotate_board = zip(*board[::-1])
                for column in rotate_board:
                    if sum(column) == 0:
                        bingo += 1

                if bingo >= 3:
                    print(cnt)
                    sys.exit()
