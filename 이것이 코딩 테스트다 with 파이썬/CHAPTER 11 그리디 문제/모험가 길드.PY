# 모험가길드

# 한 마을에 모험가 N명 있습니다.
# 공포도가 X인 모험가는 반드시 X명 이상으로 구성한 모험가 그룹에 참가해야 여행을 떠날 수 있도록 규정했습니다.
# 최대 몇 개의 모험가 그룹을 만들 수 있는지 궁금합니다.

# N = 5, 공포도 X가 2,3,1,2,2


n = int(input())
list = list(map(int, input().split()))

count = 0

list.sort()

while len(list)  != 0:
    a = list[len(list)-1]

    if a <= len(list):
        count += 1
        for i in range(a):
            list.pop()

    else :
        break

print(count)

# 풀이자체에서 틀림! 
# 작은 것부터 찾아가는 습관
