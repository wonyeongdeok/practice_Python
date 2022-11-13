def solution(time_table, n):
    answer = 0
    lst = [0 for _ in range(n)]
    for i, t in enumerate(time_table):
    	lst[i % n] += t
    answer = max(lst)
    return answer