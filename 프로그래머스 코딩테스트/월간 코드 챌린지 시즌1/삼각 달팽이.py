# 출제의도
# 주어진 문제를 푸는 로직을 구상할 수 있는지.

# n x n 크기의 2차원 배열을 만들ㅇ어서 사각형 달팽이 채우기와 유사한 방식으로 채우기를 한 뒤, 2차원 배열의
# 각 행에 있는 원소들을 차례대로 정답 배열에 담아 return 하도록 하면 됩니다.

# 풀이를 시작하기 전 달팽이 배열을 먼저 공부하고 오겠습니다.

def solution(n):
    answer = []
    arr = [[0 for _ in range(n)] for _ in range(n)]
    
    x = -1 
    y = 0
    number = 1
    
    for i in range(n):
        for j in range(i, n):
            if i % 3 == 0:
                x += 1
            elif i % 3 == 1:
                y += 1
            elif i % 3 == 2:
                x -= 1
                y -= 1
            arr[x][y] = number
            number += 1
   
    for i in range(n):
        for j in range(0, i+1):
            if arr[i][j] != 0:
                answer.append(arr[i][j])

    return answer
