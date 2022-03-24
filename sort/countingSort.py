# 모든 원소의 값이 0보다 크거나 같다고 가정
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 5, 2]
count = [0] * (max(array) + 1)

for i in range(len(array)):
	count[array[i]] += 1 # 각 데이터에 해당하는 인덱스의 값 증가
for i in range(len(count)): # count에 기록된 정렬 정보 확인
	for j in range(count[i]):
		print(i, end = ' ') # 각 데이터의 등장 횟수 만큼 인덱스 출력