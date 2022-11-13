# 1. num을 i로 나눌 경우 나머지가 0
# 2. i가 소수
# 3. 소인수 리스트에 append
# 4. 리스트 중 max값
 
# num = 13195
num = 600851475143
i = 2
integer_factorization_list = []

def multiply(arr):
    if len(arr) == 0:
        return 0
    else:
        return eval('*'.join([str(n) for n in arr]))

while True:
    tmp_integer_list = []
    if num % i == 0:
        for j in range(1, i + 1):
            if i % j == 0:
                tmp_integer_list.append(j)
            else:
                continue
        if len(tmp_integer_list) == 2:
            integer_factorization_list.append(tmp_integer_list[-1])
            print(integer_factorization_list)

    i += 1
    
    if multiply(integer_factorization_list) == num:
        break
 
print(f"max of integer_factorization_list: {max(integer_factorization_list)}")

