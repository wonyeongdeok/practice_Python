n = int(input())

# 지뢰가 표시되어 있는 판 만들기
mine_board = []
# 입력된 지뢰 개수
m = 0
for i in range(n):
    line = input()
    line_arr = []
    for s in line:
        # 입력된 문자 중 지뢰 있을 경우 up
        if s == '*':
            m += 1
        line_arr.append(s)
    mine_board.append(line_arr)

# 열려있거나 열려있지 않은 판 만들기
game_board = []
for i in range(n):
    line = input()
    line_arr = []
    for s in line:
        line_arr.append(s)
    game_board.append(line_arr)

coordinate = [[-1, -1], [-1, 0], [-1, 1],
              [0, -1], [0, 1],
              [1, -1], [1, 0], [1, 1]]

# 예제 출력하기
info_board = [[0]*n for _ in range(n)]

import itertools
for i, j in itertools.product(range(n), range(n)):
    mine_b = mine_board[i][j]
    game_b = game_board[i][j]
    # 각 [i, j] 별 인접 지뢰 개수
    detect_mine_cnt = 0
    # 지뢰 표시판에 '.' and 게임 표시판에 'x'일 경우
    if mine_b == '.' and game_b == 'x':
        # 상하좌우 혹은 대각선으로 인접한 8개의 칸에 지뢰 존재 여부 탐색
        for r, c in coordinate:
            dr = i + r
            dc = j + c
            # n x n 게임보드 외 탐색 금지
            if dr < 0 or dc < 0:
                continue
            if dr >= n or dc >= n:
                continue
            # 좌표 탐색 시 지뢰일 경우
            if mine_board[dr][dc] == '*':
                # [i][j]와 인접한 [dr][dc]에서 지뢰 발견하여 지뢰 개수 up
                detect_mine_cnt += 1
        # 상화좌우 및 대각선 인접 지뢰 개수만큼 [i][j]에 숫자 입력
        for m_number in range(m + 1):
            if detect_mine_cnt == m_number:
                info_board[i][j] = str(m_number)

    elif mine_b == '.' and game_b == '.':
        info_board[i][j] = '.'
    elif mine_b == '*' and game_b =='.':
        info_board[i][j] = '.'

    if mine_b == '*':



for info in info_board:
    res = ''.join(info)
    print(res)
