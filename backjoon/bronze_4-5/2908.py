a, b = input().split()

a_int = int(a[::-1])
b_int = int(b[::-1])
if a_int > b_int:
    print(a_int)
else:
    print(b_int)
