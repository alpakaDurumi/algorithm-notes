array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
	for j in range(i, 0, -1): # i 부터 1 까지 감소하며 반복
		if array[j] < array[j - 1]:
			array[j], array[j - 1] = array[j - 1], array[j] # swap
		else:
			break # 삽입될 데이터보다 작은 데이터를 만나면 그 위치에서 멈춘다
			# continue로 작성하면 이미 정렬이 된 상태의 데이터들을 다시 비교하게 된다
print(array)