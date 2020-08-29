# BFS 너비 우선 탐색
# 가까운 노드 부터 탐색하는 알고리즘
from collections import deque

def bfs(graph, start, visited):
    # 큐(Queue) 구현을 위해 deque 라이브러리를 사용. 
    queue = deque([start])

    visited[start] = True
    # 큐가 빌 때까지
    while queue:
        v = queue.popleft()
        print(v, end = ' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False] * 9 
bfs(graph,1,visited)