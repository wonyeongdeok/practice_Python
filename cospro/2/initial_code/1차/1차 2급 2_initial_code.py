#You may use import as below.
#import math

def solution(price, grade):
    #Write code here.
    if grade == "S":
        answer = int(price * 0.95)
    elif grade == "G":
        answer = int(price * 0.80)
    elif grade == "V":
        answer = int(price * 0.85)

    return answer

#The following is code to output testcase.
price1 = 2500
grade1 = "V"
ret1 = solution(price1, grade1)

#Press Run button to receive output.
print("Solution: return value of the function is", ret1, ".")
    
price2 = 96900
grade2 = "S"
ret2 = solution(price2, grade2)

#Press Run button to receive output.
print("Solution: return value of the function is", ret2, ".")