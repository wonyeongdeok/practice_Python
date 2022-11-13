a, b, c = map(int, input().split())
t = 0
for i in range(a):
    for j in range(b):
        for k in range(c):
            print(i, j, k)
            t += 1
print(t)