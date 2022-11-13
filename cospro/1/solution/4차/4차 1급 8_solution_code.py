def func_a(card):
    card_count = [0] * 10
    for card_i in card:
        card_count[card_i] += 1
    return card_count

num_list = []
def func_b(level, max_level, num, current_count, max_count):
    if level == max_level:
        num_list.append(num)
        return

    for i in range(1, 10):
        if current_count[i] < max_count[i]:
            current_count[i] += 1
            func_b(level + 1, max_level, num * 10 + i, current_count, max_count)
            current_count[i] -= 1

def func_c(list, n):
    if n in list:
        return list.index(n) + 1
    return -1

def solution(card, n):
    card_count = func_a(card)
    func_b(0, len(card), 0, [0] * 10, card_count)
    answer = func_c(num_list, n)
    return answer