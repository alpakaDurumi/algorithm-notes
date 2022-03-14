def dfs(graph, v, visited):
	# 현재 노드인 v를 방문했다고 표시하고 출력
	visited[v] = True
	print(v, end = ' ')
	# v에 인접한 노드 중 방문하지 않은 노드를 재귀적으로 방문
	for i in graph[v]:
		if not visited[i]:
			dfs(graph, i, visited)

# 인접 리스트 형태로 주어진 그래프
graph = [
	[],
	[2, 3, 8],
	[1, 7],
	[1, 4, 5],
	[3, 5],
	[3, 4],
	[7],
	[2, 6, 8],
	[1, 7]
]

# 각 노드가 방문된 정보를 갖는 리스트
visited = [False] * 9

dfs(graph, 1, visited)