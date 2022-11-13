
# 조건
# 1. 모든 칸 정확히 한 번씩 방문
# 2. 마지막으로 방문하는 칸에서 시작점 방문 가능해야함
# 3. 가로 A~F, 세로 1~6

# 출력
# 조건 모두 만족 시 valid, 불만족 시 invalid

# 체스판 만들기
# board = []
# for i in range(6, 0, -1):
#     tmp_board = []
#     for j in range(65, 71):
#         space = chr(j) + str(i)
#         tmp_board.append(space)
#     board.append(tmp_board)



spaces = '''A1
B3
A5
C6
E5
F3
D2
F1
E3
F5
D4
B5
A3
B1
C3
A2
C1
E2
F4
E6
C5
A6
B4
D5
F6
E4
D6
C4
B6
A4
B2
D1
F2
D3
E1
C2'''
spaces = spaces.split('\n')

# 체스판 만들기
board = []
for _ in range(6):
    tmp_board = [0 for _ in range(6)]
    board.append(tmp_board)

# 이동가능한 방향 정하기
steps = [(-2, -1), (-2, 1), (2, 1), (2, -1),
         (-1, 2), (-1, -2), (1, 2), (1, -2)]

# 가로 입력 값 숫자로 바꿀 딕셔너리 생성
alpha_dict = {chr(i): i - 65 for i in range(65, 71)}

frist_space = ''

b_dx = ''
b_dy = ''
for i, space in enumerate(spaces):
    dx = alpha_dict[space[0]]
    dy = 6 - int(space[1])

    if i == 0:
        frist_space = (dy, dx)
        board[dy][dx] = 1
        b_dx = dx
        b_dy = dy
        continue

    for step in steps:
        nx, ny = step
        tmp_dx = b_dx + nx
        tmp_dy = b_dy + ny

        if tmp_dx == dx and tmp_dy == dy:
            if board[tmp_dx][tmp_dy] == 0:
                board[dx][dy] = 1
                break

    if i == 35:
        is_true = False
        for step in steps:
            nx, ny = step
            tmp_dx = b_dx + nx
            tmp_dy = b_dy + ny
            if frist_space == (dx, dy):
                is_true = True
        if is_true:
            print('Valid')
        else:
            print('Invalid')

board
