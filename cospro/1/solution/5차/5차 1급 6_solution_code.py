numbers_int = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers_char = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def char_to_int(ch):
    for i in range(10):
        if ch == numbers_char[i]:
            return numbers_int[i]

def int_to_char(val):
    for i in range(10):
        if val == numbers_int[i]:
            return numbers_char[i]

def convert_scale(num, q):
    if num == 0:
        return ""
    return convert_scale(num // q, q) + int_to_char(num % q)

def parse_decimal(s, p):
    num = 0
    mul = 1
    for s_i in reversed(s):
        num += char_to_int(s_i) * mul
        mul *= p
    return num

def solution(s1, s2, p, q):
    num1 = parse_decimal(s1, p)
    num2 = parse_decimal(s2, p)
    answer = convert_scale(num1 + num2, q)
    return answer