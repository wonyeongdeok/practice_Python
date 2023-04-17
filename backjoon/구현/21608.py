'''
학생의 수 N^2명
(r, c) 는 r행 c열

'''

n = int(input())

rooms = [[0] * n for _ in range(n)]

# 디버깅 편의 위해 입력 한번에 받기
data = [list(map(int, input().split())) for _ in range(n ** 2)]

# 학생 번호 별 종하하는 학생의 번호를 딕셔너리 생성
like_dict = {i[0]: i[1:] for i in data}

for i, da in enumerate(data):
    # 가장 첫번째 학생이 배정 받을 자리는 무조건 (1,1)
    if i == 0:
        rooms[1][1] == da[0]
        continue

    for j in range(n ** 2):
        for k in range(n ** 2):
            if rooms[i][j] == 0:
