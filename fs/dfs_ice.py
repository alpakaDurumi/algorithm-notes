n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]

def dfs(x, y):
	# 범위를 벗어나는 경우 False를 return
	if x <= -1 or x >= n or y <= -1 or y >= m:
		return False
	# 해당 위치가 범위를 벗어나지 않으면서 1이 아닌 경우
	if graph[x][y] == 0:
		# 방문 처리
		graph[x][y] = 1
		# 인접한 노드들을 재귀적으로 방문
		dfs(x - 1, y)
		dfs(x + 1, y)
		dfs(x, y - 1)
		dfs(x, y + 1)
		# 해당 노드에서의 dfs는 True를 return
		return True
	# 범위를 벗어나지 않고 1인 경우 False를 return
	return False
	# 인접한 노드에 대해서도 방문 처리를 하게 되므로(graph[x][y]가 1이 되므로)
	# 한 묶음 당 하나의 True만이 return 된다

# 묶음의 개수를 result에 누적시킨 후 출력한다
result = 0
for i in range(n):
	for j in range(m):
		if dfs(i, j) == True:
			result += 1

print(result)
