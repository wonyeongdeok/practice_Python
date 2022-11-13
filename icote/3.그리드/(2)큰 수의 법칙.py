''' 통상적인 그리디 알고리즘 접근법'''
# n, m, k를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())
# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort() # 입력받은 수 정렬
first = data[n-1] # 첫 번째로 큰 수
second = data[n-2] # 두 번째로 큰 수

result = 0

while 1:
    for _ in range(k):# 가장 큰 수를 k번 더하기
        if m == 0: # m이 0이라면 반복문 탈출
            break
        result += first
        m -= 1 # 결과값에 첫번째 큰 수를 더할 때마다 입력된 덧셋 횟수 m에서 1씩 빼기

    if m == 0: # m이 0이라면 반복문 탈출
        break
    result += second # 두 번째로 큰 수를 한 번 더하기
    m -= 1 # 결과값에 두 번째로 큰 수를 더할 때마다 입력된 덧셈 횟수 m에서 1씩 빼기

print(result)

'''더 효율적인 해결법'''
# 만약 m의 크기가 100억 이상처럼 커진다면 시간 초과 판정을 받을 수 있음.
# 조건문을 잘 보고 변수 리미트가 억단위로 설정되어 있다면 무한반복문 또는 반복문을 사용해서는 안 된다.
# 그리디 알고리즘 문제이면서 반복문을 쓸 수 없다라는 결론에 도달하게 되는데 이럴 때는 패턴을 찾아서 수학적 원리로 접근하는 게 좋다.

# n, m, k를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())
# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort() # 입력받은 수 정렬
first = data[n-1] # 첫 번째로 큰 수
second = data[n-2] # 두 번째로 큰 수

# 가장 큰 수가 더해지는 횟수 계산
count = (m // (k + 1)) * k + m % (k + 1)

result = 0
result += count * first # 가장 큰 수 더하기
result += (m - count) * second # 두 번째로 큰 수 더하기

print(result)
