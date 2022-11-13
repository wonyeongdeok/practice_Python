def solution(korean, english):
    answer = 0
    math = 210 - (korean + english)
    if math > 100:
        answer = -1
    else:
        answer = math
    return answer