def func_a(number1, number2):
    ret = 0
    if number1 > number2:
        ret = number1 - number2
    else:
        ret = number2 - number1
    return ret

def func_b(number):
    ret = 0
    while number != 0:
        number = number // 10
        ret += 1
    return ret

def func_c(number, digit):
    ret = 0
    for i in range(digit):
        temp = number % 10
        number = number // 10
        ret = ret * 10 + temp
    return ret

def solution(number):
    answer = 0
    digit = func_b(number)
    convert_number = func_c(number, digit)
    answer = func_a(number, convert_number)
    return answer