def solution(score):
    answer = [0] * len(score)
    for i in range(len(score)):
        answer[i] = sum(map(lambda x:x > score[i], score))+1
    return answer