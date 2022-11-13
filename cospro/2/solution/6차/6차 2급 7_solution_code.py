def solution(money, chairs, desks):
    answer = 0
    for chair in chairs:
        for desk in desks:
            price = chair + desk
            if answer < price and price <= money:
                answer = price
    return answer