# 음료수 얼려먹기 
# 사실 문제 자체적으로 DFS를 사용해서 0끼리 연결되어 있는 것만 연결시켜주면 끝이다.

# N,M 을 공백으로 구분하여 입력받기

n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력받기 

graph = []

for i in range(n):
    graph.append(list(map(int, input())))

def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y > m:
        return False
    # 아직 방문하지 않은 곳이라면?
    if graph[x][y] == 0:
        graph[x][y] = 1
        # 상 하 좌 우 위치도 모두 재귀적으로 호출
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

result = 0

for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행
        if dfs(i, j) == True:
            result += 1

print(result)
        
