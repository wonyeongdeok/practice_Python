from string import ascii_lowercase

alphas = list(ascii_lowercase)

S = input()

res = []
for alpha in alphas:
    is_exist = False
    for i, s in enumerate(S):
        if alpha == s:
            is_exist = True
            res.append(str(i))
            break
    if not is_exist:
        res.append(str(-1))
print(' '.join(res))
