n = int(input())
i = 1
while i <= n:
    if i % 10 == 3:
        print('X', end=' ')
        i += 1
        continue
    elif i % 10 == 6:
        print('X', end=' ')
        i += 1
        continue
    elif i % 10 == 9:
        print('X', end=' ')
        i += 1
        continue
    else:
        print(i, end=' ')
        i += 1
