def solution(socks):
    answer = 0
    count = [0 for _ in range(10)]
    for s in socks:
        count[s] += 1
    for c in count:
        answer += (c // 2)
    return answer