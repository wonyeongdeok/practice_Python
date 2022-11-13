def solution(scores):
	people_count = 0
	pass_score = [80, 88, 70]

	for score in scores:
		pass_count = 0
		for i in range(3):
			if score[i] < pass_score[i]/2:
				pass_count = 0
				break
			elif score[i] >= pass_score[i]:
				pass_count += 1
		if pass_count >1:
			people_count += 1
	return people_count