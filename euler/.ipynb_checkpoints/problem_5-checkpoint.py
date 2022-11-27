# 나눌 수 초기 값 설정
# 1 ~ 20 사이 어떤 수로 나누어도 나머지가 0인 수 찾기
# 나누어 떨어지는 수의 개수가 총 사이의 개수와 같으면 무한 루프 브레이크

start_num = 1
end_num = 20

target_num= 0
while True:
    cnt = 0
    for i in range(start_num, end_num + 1):
        if target_num == 0:
            break
        else:
            remainder = target_num % i
            if remainder == 0:
                cnt += 1
                continue
            else:
                break
            
    if cnt == end_num:
        break
    else:
        target_num += 1
    
result = target_num
print(f"result: {result}")