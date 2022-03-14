from collections import deque

def bfs(graph, start, visited):
	# 큐 구현을 위해 deque 라이브러리 사용
	queue = deque([start])
	# 현재 노드를 방문 처리
	visited[start] = True
	# 큐가 빌 때까지 반복
	while queue:
		# 큐에서 하나의 원소를 뽑아 출력
		v = queue.popleft()
		print(v, end = ' ')
		# 뽑은 원소인 v와 인접한 노드 중 방문되지 않은 노드들을 방문 처리하며 큐에 삽입
		for i in graph[v]:
			if not visited[i]:
				queue.append(i)
				visited[i] = True

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

bfs(graph, 1, visited)