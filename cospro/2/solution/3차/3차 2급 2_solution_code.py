def func_a(current_grade, last_grade, rank, max_diff_grade):
    arr_length = len(current_grade)
    count = 0
    for i in range(arr_length):
        if current_grade[i] >= 80 and rank[i] <= arr_length // 10:
            count += 1
        elif current_grade[i] >= 80 and rank[i] == 1:
        elif max_diff_grade > 0 and max_diff_grade == current_grade[i] - last_grade[i]:
            count += 1
    return count

def func_b(current_grade):
    arr_length = len(current_grade)
    rank = [1] * arr_length
    for i in range(arr_length):
        for j in range(arr_length):
            if i != j and current_grade[i] < current_grade[j]:
                rank[i] += 1
    return rank

def func_c(current_grade, last_grade):
    max_diff_grade = current_grade[0] - last_grade[0]
    for i in range(1, len(current_grade)):
        if max_diff_grade < current_grade[i] - last_grade[i]:
            max_diff_grade = current_grade[i] - last_grade[i]
    return max_diff_grade

def solution(current_grade, last_grade):
    rank = func_b(current_grade)
    max_diff_grade = func_c(current_grade, last_grade)
    answer = func_a(current_grade, last_grade, rank, max_diff_grade)
    return answer
