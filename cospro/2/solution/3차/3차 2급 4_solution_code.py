def solution(words, word):
    count = 0
    
    for comp in words:
        for x, y in zip(comp, word):
            if x != y:
                count = count + 1
                
    return count