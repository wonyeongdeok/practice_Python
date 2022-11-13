A = [6,1,4,6,3,2,7,4]
K = 3
L = 2
# A = [10, 19, 15]
# K = 2
# L = 2
# A = [10, 19, 15]
# K = 1
# L = 1

def solution(A, K, L):
    alice = 0
    bob = 0

    for i in range(len(A)-K+1):
        tmp_alice = sum(A[i:i+K])
        if tmp_alice > alice:
            alice = tmp_alice
            alice_range = range(i, i+K)

    for i in range(len(A)-L+1):
        tmp_bob = sum(A[i:i+L])
        if tmp_bob > bob:
            bob_range = range(i, i+L)
            is_overlap = False
            for b in bob_range:
                if b in alice_range:
                    is_overlap = True
            if not is_overlap:
                bob = tmp_bob

    if alice and bob:
        ans = alice + bob
    else:
        ans = -1

    return ans

solution(A, K, L)
