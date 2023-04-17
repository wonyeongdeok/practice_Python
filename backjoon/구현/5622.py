word = input()

alpha_list = ['ABC', 'DEF', 'GHI', 'JKL',
                'MNO', 'PQRS', 'TUV', 'WXYZ']
cnt = 0
for w in word:
    for alpha in alpha_list:
        if w in alpha:
            cnt += alpha_list.index(alpha) + 3
print(cnt)
