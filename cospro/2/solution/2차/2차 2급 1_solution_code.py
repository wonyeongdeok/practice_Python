max_product_number = 10

def func_a(arr):
    max_product_number = 10
    counter = [0 for _ in range(max_product_number + 1)]
    for x in arr:
        counter[x] += 1
    return counter

def solution(left_gloves, right_gloves):
    left_counter = func_a(left_gloves)
    right_counter = func_a(right_gloves)
    
    total = 0
    for i in range(1, max_product_number + 1):
        total += min(left_counter[i], right_counter[i])
    return total