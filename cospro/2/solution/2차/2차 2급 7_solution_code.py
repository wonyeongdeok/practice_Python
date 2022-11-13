def solution(value, unit):
    converted = 0
    if unit == "C":
        value = (value * 1.8) + 32
    if unit == "F":
        value = (value - 32) / 1.8
    converted = int(value)
    return converted