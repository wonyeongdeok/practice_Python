# A = [1, 0, 1, 0, 1, 1]
# A = [1, 1, 0, 1, 1]
# A = [0, 1, 0]
A = [0, 1, 1, 0]



ans = 0
for i in range(len(A)-1):
    if i == 0:
        if A[i] == A[i+1]:
            if A[i] == 0:
                A[i] = 1
            elif A[i] == 1:
                A[i] = 0
            ans += 1
    elif i > 0:
        if A[i] == A[i+1]:
            if A[i-1] != A[i]:
                if A[i] == 0:
                    A[i+1] = 1
                elif A[i] == 1:
                    A[i+1] = 0
                ans += 1



print(A)
print(ans)



# ans = 0
# for i in range(1, len(A)):
#     if A[i] == A[i-1]:
#         if A[i] == 0:
#             A[i] = 1
#         elif A[i] == 1:
#             A[i] = 0
#         ans += 1
#
#     if A[i] != A[i-1]:
#         continue
#
# print(A)
# print(ans)


def solution(A):
    ans = 0
    for i in range(len(A)-1):
        if i == 0:
            if A[i] == A[i+1]:
                if A[i] == 0:
                    A[i] = 1
                elif A[i] == 1:
                    A[i] = 0
                ans += 1
        elif i > 0:
            if A[i] == A[i+1]:
                if A[i-1] != A[i]:
                    if A[i] == 0:
                        A[i+1] = 1
                    elif A[i] == 1:
                        A[i+1] = 0
                    ans += 1
    return ans
