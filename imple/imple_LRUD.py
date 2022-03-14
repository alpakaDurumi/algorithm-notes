n = int(input())
r = input().split()

x, y, = 1, 1

# 1. 간단한 예시
for c in r:
	if c == 'L' and y != 1:
		y -= 1
	elif c == 'R' and y != n:
		y += 1
	elif c == 'U' and x != 1:
		x -= 1
	elif c == 'D' and x != n:
		x += 1

# # 2. 방향벡터 사용
# dx = [0, 0, -1, 1]
# dy = [-1, 1, 0, 0]
# move_types = ['L', 'R', 'U', 'D']

# for c in r: # r에 있는 문자 하나씩 확인
# 	for i in range(len(move_types)): # 해당 문자의 move_types에서의 순서를 확인하여 다음 좌표 저장
# 		if r == move_types[i]:
# 			nx = x + dx[i]
# 			ny = y + dy[i]
# 	if nx < 1 or ny < 1 or nx > n or ny > n: # 범위를 벗어나는 경우, 무시하고 다음 문자 확인
# 		continue
# 	x, y = nx, ny # 다음 좌표로 이동
		
print(x, y)