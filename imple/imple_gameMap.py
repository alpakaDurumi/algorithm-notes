n, m = map(int, input().split())
x, y, d = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)] # 맵
visited = [[0] * m for _ in range(n)] # 방문 여부를 나타내는 2차원 리스트
visited[x][y] = 1 # 첫 시작 위치를 방문했다고 표시

# 북, 동, 남, 서 순서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전하는 함수
def turn_left():
    global d  # 함수 바깥에서 선언된 전역 변수인 d를 사용하기 위함
    d -= 1  # 왼쪽으로 회전
    if d == -1:  # 원래 북쪽(0)을 바라보다가 1이 감소하여 -1이 된 경우
        d = 3  # d를 서쪽(3)으로 지정

count = 1
turn_time = 0 # 회전한 횟수
while True:
	turn_left() # 먼저 회전하고
	nx = x + dx[d]
	ny = y + dy[d]
	if visited[nx][ny] == 0 and map[nx][ny] == 0: # 방문하지 않았으며, 육지라면 이동
		x = nx
		y = ny
		visited[x][y] = 1 # 방문 표시
		count += 1 # 증가
		turn_time = 0 # 0으로 초기화
		continue # 다시 회전하기 위해 다음 반복 과정으로 넘어감
	else: # 이동할 수 없는 경우
		turn_time += 1 # 회전한 횟수 증가
	if turn_time == 4: # 한바퀴 돌았다면 한칸 뒤의 좌표 계산
		nx = x - dx[d]
		ny = y - dy[d]
		if map[nx][ny] == 0: # 뒤쪽 방향이 육지라면 돌아가고
			x = nx
			y = ny
		else: # 바다라면 반복문을 종료하고 빠져나온다
			break
		turn_time = 0 # 후진한 후 회전 횟수 초기화
print(count)