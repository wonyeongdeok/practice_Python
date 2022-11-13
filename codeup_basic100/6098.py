input_string = '''1 1 1 1 1 1 1 1 1 1
1 0 0 1 0 0 0 0 0 1
1 0 0 1 1 1 0 0 0 1
1 0 0 0 0 0 0 1 0 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 0 1 0 1 0 1
1 0 0 0 0 1 0 1 0 1
1 0 0 0 0 1 0 1 0 1
1 0 0 0 0 0 1 1 1 1
1 1 1 1 1 1 1 1 1 1'''
#
# path_list = input_string.split('\n')
# path_list = [list(map(int, path.split())) for path in path_list]

path_list = list()
for _ in range(10):
    path = list(map(int, input().split()))
    path_list.append(path)

x, y = 1, 1
while True:
    # 먹이를 찾은 경우
    if path_list[x][y] == 2:
        path_list[x][y] = 9
        break
    # 더이상 움직일 수 없는 경우
    elif path_list[x+1][y] == 1 and path_list[x][y+1] == 1:
        path_list[x][y] = 9
        break
    else:
        path_list[x][y] = 9

    if path_list[x][y+1] == 1:
        x += 1
    else:
        y += 1

for path in path_list:
    path = list(map(str, path))
    print(' '.join(path))
