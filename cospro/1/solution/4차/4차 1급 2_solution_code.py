small_letters = "abcdefghijklmnopqrstuvwxyz"
big_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def convert_small(alphabet):
    for i in range(0, 26):
        if big_letters[i] == alphabet:
            return small_letters[i]
    return alphabet

def solution(s):
    answer = ''
    s_len = len(s)
    boss = convert_small(s[0])
    cnt = 1
    for i in range(1, s_len):
        if convert_small(s[i]) == boss:
            cnt += 1
        else:
            answer += boss
            answer += str(cnt)
            boss = convert_small(s[i])
            cnt = 1

    answer += boss
    answer += str(cnt)
    return answer