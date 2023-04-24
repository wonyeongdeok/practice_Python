"""
제목 : 스위치 켜고 끄기

1. 남자일 경우
 - 스위치 번호가 남학생 받은 수의 배수이면, 그 스위치의 상태를 바꿈
2. 여학생일 경우
 - 자기가 받은 수와 같은 번호가 붙은 스위치를 중심으로 좌우 대칭이면서 가장 많은 스위치
   를 포함하는 구간을 찾아서, 그 구간에 스위치 상태를 모두 바꿈
 - 대칭이 안 될 경우 자기가 받은 수와 같은 번호만 바꿈

"""

n = int(input())

switchs = list(map(int, input().split()))

students = int(input())

for student in range(students):
    sex, stu_num = list(map(int, input().split()))
    stu_num -= 1  # 리스트 접근 용이성 위해 -1
    if sex == 1:  # 남자일 경우
        for i in range(stu_num, n):
            if i % stu_num == 0 and switchs[i] == 1:
                switchs[i] = 0
            elif i % stu_num == 0 and switchs[i] == 0:
                switchs[i] = 1
    elif sex == 2:  # 여자인 경우
        fn_left_j = 0
        fn_right_j = 0
        for j in range(1, n):
            left_j = stu_num - j
            right_j = stu_num + j
            if 0 <= left_j and right_j < n:  # stu_num을 기준으로 좌 우 인덱스가 있는 경우
                if switchs[left_j] == switchs[right_j]:  # 좌우 대칭인 경우
                    fn_left_j = left_j
                    fn_right_j = right_j
                elif switchs[left_j] != switchs[right_j]:
                    
            else:  # 좌 우 인덱스 없는 경우
                if switchs[stu_num] == 1:
                    switchs[stu_num] = 0
                elif switchs[stu_num] == 0:
                    switchs[stu_num] = 1
                break