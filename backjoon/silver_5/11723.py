''' 1. 시간초과 -> 해결
- 반복문에서 입력받는 부분에 sys.stdin.readline 사용하여 시간초과 해결
- 하지만 문제 틀림... 해결중....'''

import sys
# n = int(input())
# n = int(sys.stdin.readline())
s = set()
n = '''
add 1
add 2
check 1
check 2
check 3
remove 2
check 1
check 2
toggle 3
check 1
check 2
check 3
check 4
all
check 10
check 20
toggle 10
remove 20
check 10
check 20
empty
check 1
toggle 1
check 1
toggle 1
check 1'''
n = n.strip().split('\n')
for i in n:
# for i in range(n):
    data = i
    # data = sys.stdin.readline().strip()
    if ' ' in data:
        cal, x = data.split()
        # add 연산 수행
        if cal == 'add':
            if not x in s:
                s.add(x)
        # remove 연산 수행
        elif cal == 'remove':
            if x in s:
                s.remove(x)
        # check 연산 수행
        elif cal == 'check':
            if x in s:
                print(1)
            else:
                print(0)
        # toggle 연산 수행
        elif cal == 'toggle':
            if x in s:
                s.remove(x)
            else:
                s.add(x)
    else:
        cal = data
        # all 연산 수행
        if cal == 'all':
            s = {str(i) for i in range(1, 21)}
        # empty 연산 수행
        elif cal == 'empty':
            s = set()





'''2. 해결

시간초과 1
-> all과 empty 연산 부분을 진행할지 말지 정하는 조건을 try/except로 접근했었다.
그러나 try 도중 except로 넘어가게 되면 불필요한 시간을 낭비하게 된다.
공백 유무에 따라 시도할 연산 종류를 구분지었더니 해결되었다.

시간초과 2
-> x를 str로 받기 때문에 all 연산 부분에서 str으로 i를 생성해야 output이 나온다. 하지만 시간초과에 걸린다.
i를 생성할 때마다 str으로 변환해주는 작업이 있기 때문인 듯하다.
틀렸습니다

'''''


import sys
n = int(sys.stdin.readline())
s = set()

for i in range(n):
    data = sys.stdin.readline().strip()
    if ' ' in data:
        cal, x = data.split()
        x = int(x)
        # add 연산 수행
        if cal == 'add':
            if not x in s:
                s.add(x)
        # remove 연산 수행
        elif cal == 'remove':
            if x in s:
                s.remove(x)
        # check 연산 수행
        elif cal == 'check':
            if x in s:
                print(1)
            else:
                print(0)
        # toggle 연산 수행
        elif cal == 'toggle':
            if x in s:
                s.remove(x)
            else:
                s.add(x)
    else:
        cal = data
        # all 연산 수행
        if cal == 'all':
            s = {i for i in range(1, 21)}
        # empty 연산 수행
        elif cal == 'empty':
            s = set()
