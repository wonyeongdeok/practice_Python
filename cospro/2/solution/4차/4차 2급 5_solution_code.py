def solution(calorie):
    answer = 0
    min = 1000
    
    for x in calorie:
        if min < x:
            answer += (x - min)
        else:
            min = x

    return answer