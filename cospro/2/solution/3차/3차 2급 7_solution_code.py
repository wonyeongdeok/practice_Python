def solution(a, b, k):
    answer = 0
    
    if a < (3 * b):
        answer = a // 3
    else:
        answer = b
        
    remain_a = a - 3 * answer
    remain_b = b - answer
    
    i = 0
    k = k - (remain_a + remain_b)
    
    while k > 0:
        if i % 4 == 0:
            answer = answer - 1
        i = i + 1
        k = k - 1
        
    return answer