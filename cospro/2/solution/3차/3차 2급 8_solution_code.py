def solution(tv):
    answer = 0
    
    used_tv = [0] * 25;
    for program in tv:
        for i in range(program[0], program[1]):
            used_tv[i] = used_tv[i] + 1
    
    for i in used_tv:
        if i >= 2:
            answer = answer + 1
            
    return answer