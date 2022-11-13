def solution(scores):
    return (sum(scores) - max(scores) - min(scores)) // (len(scores) - 2)