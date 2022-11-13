def solution(time_table):
    answer = 0
    first_class, last_class = 0, 0
    for i in time_table:
        if i == 1:
            first_class = i
            break
    for i in reversed(time_table):
        if i == 1:
            last_class = i
            break
    for i in range(first_class, last_class):
        if time_table[i] == 0:
            answer += 1
    return answer