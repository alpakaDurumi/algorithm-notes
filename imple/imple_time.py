n = int(input())
count = 0
for i in range(n + 1): # 시
	for j in range(60): # 분
		for k in range(60): # 초
			time = str(i) + str(j) + str(k) # 하나의 문자열로 합쳐서
			if '3' in time: # 3이 포함되었는지 확인
				count += 1 # 포함되었다면 count에 1 누적
print(count)