l = input()
row = int(l[1]) # 행
column = int(ord(l[0])) - int(ord('a')) + 1 # 열 : ord()와 int()를 통해 입력된 문자가 a인 경우 정수 1로 대응되게 만드는 과정
steps = [(-2, 1), (-2, -1), (2, 1), (2, -1), (1, -2), (1, 2), (-1, -2), (-1, 2)]
count = 0

for step in steps:
	next_row = row + step[0]
	next_column = column + step[1]
	if 1 <= next_row <= 8 and 1 <= next_column <= 8: # 나이트의 다음 위치가 정원 내부에 위치하는 경우
		count += 1
print(count)