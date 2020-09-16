n, m = map(int, input().split())
data = list(map(int, input().split()))


# 예시 1번
# N = 5 이고 M = 3 이며 각각의 무게가 차례대로 1,3,2,3,2
# (1,2),(1,3),(1,4),(1,5),(2,3),(2,5),(3,4),(4,5)

# 1부터 10까지의 무게를 담을 수 있는 리스트
array = [0] * 11

for x in data:
    # 각 무게에 해당하는 볼링공의 개수 카운트
    array[x] += 1

result = 0
# 1부터 m까지의 각 무게에 대하여 처리
for i in range(1, m + 1):
    n -= array[i] # 무게가 i인 볼링공의 개수(A가 선택할 수 있는 개수) 제외
    result += array[i] * n # B가 선택하는 경우의 수와 곱해주기

print(result)
