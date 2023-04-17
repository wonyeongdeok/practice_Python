while 1:
    try:
        tmp_list = input().split('\n')
        for ab in tmp_list:
            a, b = ab.split()
            print(int(a) + int(b))
    except:
        break
