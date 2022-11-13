a, b = map(int, input().split())

if a < b:
    res = b - a
    if res <= 100000:
        print(res - 1)
        for i in range(a+1, b):
            print(i, end=' ')
elif a == b:
    print(0)
else:
    res = a - b
    if res <= 100000:
        print(res - 1)
        for i in range(b+1, a):
            print(i, end=' ')
