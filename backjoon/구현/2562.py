n = 0
id = 0

for i in range(1, 10):
    tmp_n = int(input())
    if n < tmp_n:
        n = tmp_n
        id = i

print(n)
print(id)
