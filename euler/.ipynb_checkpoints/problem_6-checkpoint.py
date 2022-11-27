# 자연수 시작 값과 끝 값 설정
# 시작 값부터 끝 값까지의 합의 제곱과 제곱의 합 따로 구하기
# 합의 제곱과 제곱의 합 차이 구하기

start_num = 1
end_num = 100

sum_of_square = 0
for i in range(start_num, end_num + 1):
    sum_of_square += i ** 2

natural_num_sum = 0
for j in range(start_num, end_num + 1):
    natural_num_sum += j
square_of_sum = natural_num_sum ** 2

print(f'square_of_sum: {square_of_sum}')
print(f'sum_of_square: {sum_of_square}')

result = square_of_sum - sum_of_square
print(f"result: {result}")