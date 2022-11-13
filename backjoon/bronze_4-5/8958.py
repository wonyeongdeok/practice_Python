n = int(input())
for _ in range(n):
    ox = input()
    o_list = []
    o_cnt = 0
    for o_x in ox:
        if o_x == 'O':
            o_cnt += 1
            o_list.append(o_cnt)
        elif o_x == 'X':
            o_cnt = 0
    print(sum(o_list))
