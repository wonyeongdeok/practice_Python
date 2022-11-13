# A = [2,2,3,4,3,3,2,2,1,1,2,5]
A = [-3, -3]
# A = [1,2,3,2,1]



# hill 조건
# valley 조건

def solution(A):
    cnt = 1
    is_asc = True
    is_all_same_value = True

    for i in range(len(A)):
        if i > 0:
            if A[i-1] > A[i]:
                is_asc = False
                break
            elif A[i-1] < A[i]:
                is_asc = True
                break

    for i in range(len(A)):
        if i > 0:
            if A[i] != A[0]:
                is_all_same_value = False

            if is_asc:
                if A[i-1] > A[i]:
                    is_asc = False
                    cnt += 1
            else:
                if A[i-1] < A[i]:
                    is_asc = True
                    cnt += 1

            if i == len(A) -1 and not is_all_same_value:
                cnt += 1

    return cnt

solution(A)
