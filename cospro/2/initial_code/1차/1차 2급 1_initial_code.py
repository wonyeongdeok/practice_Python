def solution(shirt_size):
    size_counter = [0 for _ in range(6)]
    for size in shirt_size:
        if size == 'XS':
            size_counter[0] += 1
        elif size == 'S':
            size_counter[1] += 1
        elif size == 'M':
            size_counter[2] += 1
        elif size == 'L':
            size_counter[3] += 1
        elif size == 'XL':
            size_counter[4] += 1
        elif size == 'XXL':
            size_counter[5] += 1
    return size_counter      

#The following is code to output testcase.
shirt_size = ["XS", "S", "L", "L", "XL", "S"]
ret = solution(shirt_size)
 
#Press Run button to receive output.
print("Solution: return value of the function is ", ret, " .")

