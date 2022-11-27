# 소수 구하기
# 10,001번째 소수를 발견하면 스탑
target_idx = 10001
prime_num_list = list()
i = 1
while True:
    cnt = 0
    for j in range(1, i + 1):
        if i % j == 0:
            cnt += 1
        else:
            continue
    
    if cnt == 2:
        prime_num_list.append(i)
    
    if len(prime_num_list) == target_idx:
        break
    else:
        i += 1

result = prime_num_list[-1]
print(f"result: {result}")