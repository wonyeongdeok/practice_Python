def solution(schedule):
    answer = []
    for idx, i in enumerate(schedule):
        if i == "X":
            answer.append(idx+1)
    return answer