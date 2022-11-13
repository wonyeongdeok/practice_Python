def solution(words):
    answer = ""
    for w in words:
        if len(w) >= 5:
            answer += w
    if len(answer) < 1:
        answer = "empty"
    return answer