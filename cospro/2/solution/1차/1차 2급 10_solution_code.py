def solution(data):
    total = sum(data)
    average = total / len(data)
    cnt = 0
    for d in data:
        if d <= average:
            cnt += 1
    return cnt