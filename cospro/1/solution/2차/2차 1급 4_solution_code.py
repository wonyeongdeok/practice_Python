def solution(arr, K):
    n = len(arr)
    count = 0
    for p in range(0, n):
        for q in range(p + 1, n):
            for r in range(q + 1, n):
                if (arr[p] + arr[q] + arr[r]) % K == 0:
                    count += 1
    return count