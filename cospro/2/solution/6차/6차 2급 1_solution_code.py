def solution(temperature, A, B):
    answer = 0
    for i in range(A+1, B):
        if temperature[i] > temperature[A] and temperature[i] > temperature[B]:
            answer += 1
    return answer