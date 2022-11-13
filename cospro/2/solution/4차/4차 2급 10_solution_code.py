def solution(scores, cutline):
    answer = 0
    for s in scores:
        if s >= cutline:
            answer += 1
    return answer