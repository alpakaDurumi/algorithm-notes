from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]

# 방향벡터 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
	queue = deque()
	# 튜플 (x, y)를 큐에 append	
	queue.append((x, y))
	# 큐가 빌 때까지 반복
	while queue:
		x, y = queue.popleft()
		# 상하좌우의 각 네 방향으로의 다음 위치 확인(nx, ny)
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			# 범위를 벗어난 경우 continue
			if nx <= -1 or ny <= -1 or nx >= n or ny >= m:
				continue
			# 괴물을 만나게 되는 경우 continue
			if graph[nx][ny] == 0:
				continue
			# 1인 경우(해당 노드를 처음 방문하는 경우)
			# 시작 지점으로부터의 거리에 따라 graph[x][y]의 값이 1씩 증가함
			if graph[nx][ny] == 1:
				graph[nx][ny] = graph[x][y] + 1
				# 다음 위치를 다시 enqueue한다
				queue.append((nx, ny))
	# 가장 오른쪽 아래까지의 최단 거리를 반환
	return graph[n - 1][m - 1]

print(bfs(0, 0))