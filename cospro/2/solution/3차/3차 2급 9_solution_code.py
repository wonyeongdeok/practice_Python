def solution(day, numbers):
    count = 0
    for number in numbers:
        if number%2 == day%2:
            count += 1
    return count