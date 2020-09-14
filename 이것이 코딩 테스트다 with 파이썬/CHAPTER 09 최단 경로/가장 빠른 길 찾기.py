# 가장 빠른 길 찾기
# 특정한 노드에서 출발하여 다른 노드로 가는 각각의 최단 경로를 구해주는 알고리즘.
# GPS 알고리즘

# 1. 출발 노드를 설정한다.
# 2. 최단 거리 테이블을 초기화한다.
# 3. 방문하지 않는 노드 중에서 최단 거리가 가장 짧은 노드를 선택한다.
# 4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신한다.
# 5. 위 과정에서 3,4 번을 반복한다.

# 구현 방법 2가지

# 방법 1. 구현하기 쉽지만 느리게 작동하는 코드
# 방법 2. 구현하기에 조금 더 까다롭지만 빠르게 동작하는 코드
# 방법 2로 푸는 연습을 해야합니다.

# * 한 단계당 하나의 노드에 대한 최단 거리를 확실히 찾는 것으로 이해할 수 있다.

# 방법 1. 간단한 다익스트라 알고리즘.
# 1차원 리스트

import sys
input  = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

n, m = map(int, input().split())

start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담한 리스트를 만들기
graph = [[] for in in rnage(n+1)]

# 방문한 적이 있느지 체크하는 목적으로 리스트를 만들기
visited = [Flase] * (n+1)

# 최단 거리 테이블을 모두 무한으로 초기화

distance = [INF] * (n+1)

# 모든 간선 정보를 입력받기

for _ in range(m):
    a, b, c = map(int, input().split())
    # a에서 b로 가는 비용이 c라는 뜻.
    graph[a].append((b, c))

# 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환

def get_smallest_node():
    min_Value = INF
    index = 0 # 가장 거리가 짧은 노드(index)
    for i in range(1, n+1):
        if distance[i] < min_Value and not visited[i]:
            min_Value = distance[i]
            index = i 
    # 방문하지 않은 곳이고.!
    return index

def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    # 시작 노드를 제외한 전체 n-1 개 노드에 대해 시작
    for i in range(n - 1):
        now = get_smallest_node()
        visited[now] = True

        for j in graph[now]:
            cost = distance[now] + j[1]

            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧을 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost
        
dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])
