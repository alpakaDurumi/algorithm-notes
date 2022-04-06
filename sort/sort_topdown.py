# 수의 개수n, 수열 입력받기
n = int(input())
array = [int(input()) for _ in range(n)]

# 내림차순으로 정렬
result = sorted(array, reverse = True)

# 출력
for i in result:
	print(i, end = ' ')
