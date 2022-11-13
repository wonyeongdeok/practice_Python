def solution(commands):
    current_position = [0, 0]
    for d in commands:
        if d == "L":
            current_position[0] -= 1
        elif d == "R":
            current_position[0] += 1
        elif d == "U":
            current_position[1] += 1
        elif d == "D":
            current_position[1] -= 1
    return current_position