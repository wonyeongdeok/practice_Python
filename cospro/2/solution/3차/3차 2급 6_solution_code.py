def solution(length):
    answer = ''
    com = 'RRRGGB'
    if length%6 ==1 or length%6 ==2 or length%6 ==4:
        answer = '-1'
    else:
        for i in range(length):
            answer+=com[i % 6]
    return answer