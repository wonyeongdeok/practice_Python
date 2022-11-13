def solution(n, votes):
    answer = 0
    votes_len = len(votes)
    candidate = votes[0]
    count = 1
    for i in range (1, votes_len) :
        if candidate == votes[i] :
            count += 1
        else :
            count -= 1
        if count == 0 :
            candidate = votes[i]
            count = 1

    test_count = 0
    for i in range(0, votes_len) :
        if votes[i] == candidate :
            test_count += 1

    if test_count > votes_len // 2 :
        answer = candidate
    else :
        answer = -1
        
    return answer