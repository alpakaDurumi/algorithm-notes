n, k = map(int, input().split())
count = 0

# 쉬운 방법이지만, n이 큰 수인 경우 연산시간 증가
# while n > 1:
# 	if n % k == 0:
# 		n //= k
# 		count += 1
# 	else:
# 		n -= 1
# 		count += 1

while True:
	target = n // k * k # k로 나누어 떨어지는 수가 될 때까지 1씩 빼는 것을 한 번에 수행하기
	count += n - target # n에서 (n에서 1씩 빼서 나온 k로 나누어 떨어지는 수)를 빼서 1을 뺀 횟수를 얻어 누적
	n = target # n을 갱신

	if n < k: # n이 k보다 작아지면 반복문으 빠져나옴
		break

	n //= k # n을 k로 나누기
	count += 1 # 횟수 1 누적

count += n - 1 # n과 1의 차이만큼을 누적하면 끝

print(count)