def solution(hour, minute):
    hour_pos = float(hour) * 30.0 + float(minute) * 0.5
    minute_pos = float(minute) * 6.0
    answer = abs(hour_pos - minute_pos)
    if answer > float(360) - answer :
        answer = float(360) - answer
    return "{:.1f}".format(answer)