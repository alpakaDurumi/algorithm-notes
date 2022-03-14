n, m = map(int, input().split()) # 행과 열의 수 입력받기

smallest = [] # 각 행에서의 가장 작은 수를 저장하기 위한 리스트
for i in range(n): # 각 행에서 반복(n번 반복)
	data = map(int, input().split()) # 각 행에 해당하는 수들을 입력받아
	smallest.append(min(data)) # 해당 행에서 가장 작은 수를 리스트에 append

print(max(smallest)) # 리스트에서 가장 큰 값을 print