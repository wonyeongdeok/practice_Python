def solution(money, price, n):
    answer = 0
    empty_bottle = answer = money // price
    while n <= empty_bottle:
        empty_bottle = empty_bottle - n
        answer += 1
        empty_bottle += 1
    return answer