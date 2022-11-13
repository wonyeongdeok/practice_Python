word = input()

w_cnt = {}
for w in word:
    w = w.upper()
    if w not in w_cnt.keys():
        w_cnt[w] = 0
        w_cnt[w] += 1
    else:
        w_cnt[w.upper()] += 1

max_cnt = max(w_cnt.values())
if list(w_cnt.values()).count(max_cnt) > 1:
    print('?')
else:
    cnt_w = {}
    for w, cnt in w_cnt.items():
        cnt_w[cnt] = w
    print(cnt_w.get(max_cnt))
