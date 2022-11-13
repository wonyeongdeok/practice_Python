def solution(password):
    length = len(password)
    for i in range(length - 2):
        first_check = ord(password[i + 1]) - ord(password[i])
        second_check = ord(password[i + 2]) - ord(password[i+1])
        if first_check == second_check and (first_check == 1 or first_check == -1):
            return False
    return True

'''테케 만들때 맨 처음 3개만 증가인경우 마지막 3개만 증가인경우 감소인경우 숫자 알파벳등등으로 추가할것'''