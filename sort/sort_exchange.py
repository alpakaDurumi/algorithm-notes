# 입력 받기
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# a는 오름차순, b는 내림차순으로 정렬
a.sort()
b.sort(reverse = True)

# k번 수행
for i in range(k):
	# a의 원소가 b의 원소보다 작다면
	if a[i] < b[i]:
		# swap
		a[i], b[i] = b[i], a[i]
	# 아니라면 반복문을 탈출
	else:
		break

# a의 원소들의 합 출력
print(sum(a))