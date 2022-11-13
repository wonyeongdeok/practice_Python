def solution(prices):
    inf = 1000000001;
    mn = inf
    ans = -inf
    for price in prices:
        if mn != inf:
            ans = max(ans, price - mn)
        mn = min(mn, price)
    return ans
