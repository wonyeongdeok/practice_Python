def solution(papers, K):
    length = len(papers)
    for i, paper in enumerate(papers):
        K -= paper
        if K < 0:
            return i
    return length