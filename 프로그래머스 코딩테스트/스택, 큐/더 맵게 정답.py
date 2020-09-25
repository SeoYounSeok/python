# 시간 초과가 걸리기 때문에 우선순위 큐를 사용해야합니다.

import heapq
# 선입선출 개념인 우선순위 큐를 사용한 내용입니다. 

def solution(scoville,K):
    answer = 0
    # 정렬해주지만, 저기안에서는 안해주자나?..
    heapq.heapify(scoville)
    
    while scoville[0] < K :
        if len(scoville) > 1:
            num1 = heapq.heappop(scoville)    
            num2 = heapq.heappop(scoville) * 2
            
            heapq.heappush(scoville,  num1+num2)
            answer += 1
        else : 
            return -1
    
    return answer
