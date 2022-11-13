def solution(weight, boxes):
    answer = 0
    for x in boxes:
        if x < weight * 9 / 10 or x > weight * 11 / 10:
            answer += 1
    return answer