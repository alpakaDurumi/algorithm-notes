n = int(input())
array = []

# n명 입력받기
for i in range(n):
	# 공백을 두고 입력받기
	input_data = input().split()
	# 앞 입력은 문자열 그대로, 뒤 입력은 정수형으로 변환하여 저장	
	array.append((input_data[0], int(input_data[1])))

# key값에 lambda funcion 이용한 정렬
array = sorted(array, key = lambda student: student[1])

# 이름만을 출력
for student in array:
	print(student[0], end = ' ')