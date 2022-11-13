def solution(classes, m):
	count = 0
	for num in classes:
		while num > 0:
			num -= m
			count += 1
	return count