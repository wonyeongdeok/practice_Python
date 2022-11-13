
'''내가 작성한 답안 - 약 12분 걸림'''
n, k = map(int, input().split())
res = 0

while 1:
    if n == 1:
        break
    else:
        if n % k == 0:
            n //= k
        else:
            n -= 1

    res += 1

print(res)

'''나동빈님 교재 단순하게 푸는 답안 '''
n, k = map(int, input().split())
result = 0

# n이 k 이상이라면 k로 계속 나누기
while n >= k:
    # n이 k로 나누어 떨어지지 않는다면 n에서 1씩 빼기
    while n % k != 0:
        n -= 1
        result += 1
    # k로 나누기
    n //= k
    result += 1

# 마지막으로 남은 수에 대하여 1씩 빼기
while n > 1:
    n -= 1
    result += 1

print(result)


'''답안 예시'''
n, k = map(int, input().split())
result = 0
while True:
    # (n == k로 나누어떨어지는 수)가 될 때까지 1씩 빼기
    target = (n // k) * k
    result += (n - target)
    n = target

    # n이 k보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    # k로 나누기
    n //= k
    result += 1
    print(result)

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n - 1)
print(result)

# 훔...이해 안 됨.. 이게 왜 더 좋은 답안이지?..
# 그리고 어떻게 작동하는지 잘 모르겠네






















\
