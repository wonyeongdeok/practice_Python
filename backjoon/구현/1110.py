n = int(input())
tmp_n = str(n)

cnt = 0
while 1:
    if len(tmp_n) == 2:
        tmp_n = tmp_n[-1] + str(int(tmp_n[0]) + int(tmp_n[1]))[-1]
        cnt += 1
        if int(tmp_n) == n:
            break
    elif len(tmp_n) == 1:
        tmp_n = '0' + tmp_n
        tmp_n = tmp_n[-1] + str(int(tmp_n[0]) + int(tmp_n[1]))[-1]
        cnt += 1
        if int(tmp_n) == n:
            break

print(cnt)
