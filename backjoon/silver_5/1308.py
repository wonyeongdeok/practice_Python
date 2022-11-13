import datetime as dt

today = input()
d_day = input()

today_split = list(map(int, today.split()))
today = dt.datetime(today_split[0], today_split[1], today_split[2])

dday_split = list(map(int, d_day.split()))
dday = dt.datetime(dday_split[0], dday_split[1], dday_split[2])

day_gap = (dday - today).days

# 윤년 또는 평년에 따른 1년 일수 계산하여 1000년 간의 날들 구하기
limit_day = 0
for y in range(today_split[0], today_split[0] + 1000):
    is_leap_year = False
    if y % 4 == 0:
        is_leap_year = True
    if y % 100 == 0:
        is_leap_year = False
    if y % 400 == 0:
        is_leap_year = True

    if is_leap_year:
        limit_day += 366
    else:
        limit_day += 365

# 오늘부터 1000년 간의 날들(limit_day)이 오늘의 날짜와 D-Day인 날짜의 gap 보다 큰지 작은지에 따른 출력
if day_gap >= limit_day:
    print('gg')
else:
    print(f'D-{day_gap}')
