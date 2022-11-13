def solution(arr):
    dp = [1 for _ in range(len(arr))]
    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            dp[i] = dp[i-1] + 1
    answer = max(dp)
    return answer