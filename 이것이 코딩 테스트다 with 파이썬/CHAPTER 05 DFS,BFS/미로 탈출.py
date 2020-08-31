# 미로 탈출
# BFS는 시작 지점부터 가까운 노드부터 차례대로 그래프의 모든 노드를 탐색하기 때문이다.

from collections import dequq

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 이동할 4개의 방향 정의 
# 좌우하상
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    # x, y를 넣어줍니다. 
    while queue:
        x,y = queue.popleft()
        # 현제 위치에서 네방향으로 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n, ny >= m : 
                continue
            if graph[nx][ny] == 0 :
                continue
            if graph[nx][ny] == 1 :
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    return graph[n-1][m-1]
    
print(bfs(0, 0))