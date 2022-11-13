n = int(input())

for i in range(n, 0, -1):
    blank = ' ' * (n - i)
    star = '*' * i
    print(blank+star)
