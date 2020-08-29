# DFS메서드 정의
def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    # graph[v] 리스트에 리스트 값으로 들어가있고..?
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
# 2차원 리스트
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

# False 로 초반 설정 하는 것
visited = [False] * 9
dfs(graph, 1, visited)