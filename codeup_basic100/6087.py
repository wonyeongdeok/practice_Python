n = int(input())
i = 1
while n >= i:
    if i % 3 == 0:
        i += 1
        continue
    else:
        print(i, end=' ')
        i += 1
    