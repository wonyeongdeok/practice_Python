def solution(N, M):
    total = 0
    for x in range(N, M + 1):
        if x % 2 == 0:
            total += x*x
    return total