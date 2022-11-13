def solution(n):
	answer = ''
	for i in range(n):
		answer += str(i%9 + 1)
		answer = reverse(answer)
	return answer

def reverse(number):
	reverse_number = ''
	reverse_number = reverse_number.join(reversed(number))
	return reverse_number