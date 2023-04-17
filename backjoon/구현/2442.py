n = int(input())

for i in range(1, n+1):
    space = ' ' * (n - i)
    star = ('*' * i) + ('*' * (i - 1))
    res = space + star
    print(res)
