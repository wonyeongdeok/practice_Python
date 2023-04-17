a = int(input())
b = int(input())
c = int(input())

abc = str(a * b * c)

for i in range(10):
    res = 0
    for n in abc:
        if n == str(i):
            res += 1
    print(res)
