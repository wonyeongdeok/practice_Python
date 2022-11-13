n = int(input())
n_list = list(map(int, input().split()))

n_min = 0
for i in range(n):
    if i == 0:
        n_min = n_list[i]
    else:
        if n_min > n_list[i]:
            n_min = n_list[i]
        else:
            continue
print(n_min)
