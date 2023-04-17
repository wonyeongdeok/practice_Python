while 1:
    try:
        words = input()
        words_split = words.split('\n')
        for w in words_split:
            print(w)
    except:
        break
