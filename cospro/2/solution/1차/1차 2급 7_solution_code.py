def solution(scores):
    count = 0
    for i in range(len(scores)):
        if 650 <= scores[i] < 800:
            count += 1
    return count