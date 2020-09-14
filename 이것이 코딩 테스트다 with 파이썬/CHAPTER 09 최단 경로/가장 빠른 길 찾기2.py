# 현재 가장 가까운 노드를 저장하기 위한 목적으로 만 우선순위 큐를 추가로 이용
# 최단 거리가 가장 짧은 노드를 선택하는 과정을 다익스트라 최단 경로 함수안에서 우선순위큐를 사용하는 방식으로 대체할 수 있기 때문이다.
# 우선순위 큐

# 모듈 임포드 
# import heapq

# 최소 힙 생성
# 우선 순위 큐이므로, push랑 pop 생각

import heapq
import sys
input  = sys.stdin.readline
INF = int(1e9)

distance = [INF] * (n + 1)

def dijksatra(satrt):
    # 리스트를 최소 힙처럼 다룰 수 있도록 도와주는 것입니다.(java 의 우선순위 큐 클래스가 아님)
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0 으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q: # q 가 비어있지 않다면,
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now  =  heapq.heappop(q)
        # 0 , 1 => 1번 노드 도착 0

        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        # 1,2,2 / 1,3,5
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 노드들을 확인
        for i in graph[now]:
            # 2, 2 / 3, 5
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우.
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
                


