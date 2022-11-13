n = int(input())

for i in range(n+1):
    if i == 0:
        res = 0
        n_2 = res
    elif i == 1:
        res = 1
        n_1 = res
    else:
        res = n_1 + n_2
        n_2 = n_1
        n_1 = res
print(res)
