n = int(input())

go_board_list = [[0 for _ in range(19)] for _ in range(19)]

for i in range(n):
    x, y = map(int, input().split())
    x, y = x-1, y-1
    go_board_list[x][y] = 1

for row in go_board_list:
    row = map(str, row)
    result = ' '.join(row)
    print(result)
