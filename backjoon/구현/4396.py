"""
[문제]
1. n x n 격자 위 지뢰찾기
2. m개의 지뢰
3. 플레이어 격자 건드리기
    - 지뢰가 있는 지점, 패배
    - 지뢰가 없는 지점, 상하좌우 및 대각선으로 인접한 8개 칸에 지뢰 몇개인지 알려주는 0~8 나타남
"""

"""
[Solution]
1. 지뢰 격자판 생성
2. 플레이 격자판 생성
3. 출력 격자판 생성
    - 지뢰 격자판과 플레이 격자판 비교
        - 지뢰 칸이 하나라도 열려있으면 지뢰가 있는 모든 칸이 별표로 표시됨. 다른 모든 지점은 온점으로 표시됨.
        - 상하좌우 및 대각선 인접 8칸에서 지뢰 개수를 해당 격자의 숫자로 지정
"""

n = int(input('> '))

# 지뢰 격자판 생성
mine_board = []
for _ in range(n):
    mine_row = [_ for _ in input('지뢰 격자판 입력 > ')]
    mine_board.append(mine_row)

# 플레이 격자판 생성
play_board = []
for _ in range(n):
    play_row = [_ for _ in input('플레이 격자판 입력 > ')]
    play_board.append(play_row)

# 인접 8칸 이동 방향
direction_rows    = [0, 0, 1, 1, 1, -1, -1, -1]
direction_columns = [-1, 1, -1, 0, 1, -1, 0, 1]

# 출력 격자판 생성
board = [[0 for _ in range(n)] for _ in range(n)]
is_lose = False
for i in range(n):
    for j in range(n):
        # 열었는데 지뢰 칸인 경우
        if play_board[i][j] == 'x' and mine_board[i][j] == '*':
            is_lose = True
            break
        # 열었는데 숫자칸인 경우
        elif play_board[i][j] == 'x' and  mine_board[i][j] == '.':
            mine_cnt = 0
            for k in range(n):
                check_row    = i + direction_rows[k]
                check_column = j + direction_columns[k]
                # 공간을 벗어나는 경우 무시
                if check_row < 0 or check_column < 0 or check_row > n-1 or check_column > n-1:
                    continue
                if mine_board[check_row][check_column] == '*':
                    mine_cnt += 1
            board[i][j] = mine_cnt
        # 안 열려있는 경우
        else:
            board[i][j] = '.'


    # 패배 시 출력 격자를 지뢰 격자로 대체0
    if is_lose:
        board = mine_board
        break

for b in board:
    b = map(str, b)
    print(''.join(b))