n = int(input())

# [[i, j], ...] => i : 소가 어느 길에 등장했는지, j: 위치 변경 횟수
cows = [[-1, 0] for _ in range(n+1)]

for i in range(1, n+1):
    cow_num, lr = map(int, input().split())
    # 소가 어느 길에서 관찰되었는지
    if cows[cow_num][0] == -1:
        # 한번도 관찰 된 적 없는 경우 처음 등장한 길의 번호를 등록
        cows[cow_num][0] = lr
    else:
        if cows[cow_num][0] == 0 and lr == 1:
            # 길 바꾼 횟수 업데이트
            cows[cow_num][1] += 1
            # 새로 관찰된 길의 번호 등록
            cows[cow_num][0] = lr
        elif cows[cow_num][0] == 1 and lr == 0:
            cows[cow_num][1] += 1
            cows[cow_num][0] = lr

# 우치 변경 횟수 합산
res = 0
for cow in cows:
    res += cow[1]
print(res)
