# 세 자리 수의 시작값 설정
# 두 값 곱하기
# 대칭수 리스트 담기
# 리스트 중 맥스 값

start_num = 100
end_num = 1000

def check_palindrome(multiply_num):
    str_num = str(multiply_num)
    reversed_str_num = str_num[::-1]
    if reversed_str_num == str_num:
        return True
    else:
        return False

palindrome_arr = list()
for i in range(start_num, end_num):
    for j in range(start_num, end_num):
        multiply_num = i * j
        if check_palindrome(multiply_num):
            palindrome_arr.append(multiply_num)
            
result = max(palindrome_arr)
print(f"max of palindrome_arr: {result}")
            