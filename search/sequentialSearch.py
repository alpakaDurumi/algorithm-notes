# 순차 탐색
def sequential_search(n, target, array):
	for i in range(n):
		if array[i] == target:
			return i + 1

print("생성할 원소 개수와 찾을 문자열을 공백을 두고 입력")
input_data = input().split()
n = int(input_data[0])
target = input_data[1]

print("입력한 원소 개수만큼 공백을 두고 문자열 입력")
array = input().split()

print(sequential_search(n, target, array))