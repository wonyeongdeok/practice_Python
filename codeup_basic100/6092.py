# # 제출코드
#  n = int(input())
#  ran = input().split()
#  
#  out_list = [0 for _ in range(23)]
#  
#  for num in ran:
#      out_list[int(num) - 1] += 1
#  
#  for out in out_list:
#      print(out, end=' ')


# 예시 코드
n = int(input())
a = input().split()

for i in range(n):
    a[i] = int(a[i])
    
d = list()
for i in range(24):
    d.append(0)

for i in range(n):
    d[a[i]] += 1

for i in range(1, 24):
    print(d[i], end=' ')