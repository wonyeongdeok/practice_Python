h, b, c, s = map(int, input().split())
t = h * b * c * s
mb = t / 8 / 1024 / 1024
print('%.1f MB' %mb)