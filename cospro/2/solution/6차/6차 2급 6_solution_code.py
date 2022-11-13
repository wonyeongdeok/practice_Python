def solution(password):
    capital_count, small_count, digit_count = 0, 0, 0
    for p in password:
        if p >= 'A' and p <= 'Z':
            capital_count += 1
        elif p >= 'a' and p <= 'z':
            small_count += 1
        elif p >= '0' and p <= '9':
            digit_count += 1
    if capital_count >= 1 and small_count >= 2 and digit_count >= 2:
        answer = True
    else:
        answer = False
    return answer