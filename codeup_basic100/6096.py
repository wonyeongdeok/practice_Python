
# string = input().split('\n')
# s_list = list()
# for s in string:
#     s = s.replace('\r', '')
#     s = list(map(int, s.split()))
#     s_list.append(s)
# s_list

go_board_list = list()
for _ in range(19):
    row = list(map(int, input().split()))
    go_board_list.append(row)

n = int(input())
for _ in range(n):
    x, y = input().split()
    x, y = int(x)-1, int(y)-1

    for i in range(19):
        if go_board_list[x][i] == 0:
            go_board_list[x][i] = 1
        elif go_board_list[x][i] == 1:
            go_board_list[x][i] = 0

    for j in range(19):
        if go_board_list[j][y] == 0:
            go_board_list[j][y] = 1
        elif go_board_list[j][y] == 1:
            go_board_list[j][y] = 0

for xy_list in go_board_list:
    print(' '.join(list(map(str, xy_list))))
