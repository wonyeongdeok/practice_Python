n = int(input())

for _ in range(n):
    r, S = input().split()
    for s in S:
        print(s * int(r), end='')
    print()
