# 숫자 카드 게임 

n, m = map(int, input().split())

result = 0

for i in range(n) : 
    data = list(map(int, input()))
    # 행의 최소값 찾기
    min_value = min(data)
    result = max(result, min_value)

print(result)

