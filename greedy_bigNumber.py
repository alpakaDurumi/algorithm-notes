n, m, k = map(int, input().split())			# 배열의 크기, 숫자가 더해지는 횟수, 연속해서 더해질 수 있는 횟수
numbers = list(map(int, input().split()))	# 수 입력받기
numbers.sort(reverse = True)				# 내림차순으로 정렬

first = numbers[0]
second = numbers[1]

sum = 0
# while True:
# 	for i in range(k):						# k번 first를 더함
# 		if m == 0:							# 횟수가 0번 남을 시 for문 밖으로 빠져나옴
# 			break
# 		sum += first
# 		m -= 1
# 	if m == 0:
# 		break
# 	sum += second
# 	m -= 1

count = m // (k + 1) * k + m % (k + 1)	# k개의 first와 1개의 second로 이루어진 수열이 몇 번 반복되는지를 계산하면서 first의 개수 구하기
sum += count * first
sum += (m - count) * second
print(sum)
