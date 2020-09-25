# 실패 코드. 

def solution(scoville, K):
    answer = 0
    count = 0
    scoville.sort()
    if scoville[0] < K and len(scoville) <= 1:
        return -1
    
    if scoville[0] >= K:
        return 0
    # 낮은 값들만 가능하다고 생각했습니다. 1번 ㅎㅎㅎ
    #while scoville[0] < K and scoville[1] < K:
    while scoville[0]< K or len(scoville) > 1:
        num1 = scoville.pop(0)
        num2 = scoville.pop(0)
        
        if K < num1 + num2 * 2:
            count += 1
            break
        else:
            if len(scoville) <= 1:
                return -1
            count += 1
            scoville.append(num1 + num2 * 2)
            scoville.sort()

    return count
