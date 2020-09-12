# 실전 문제 : 부품 찾기
# 2중 포문을 썼을 때.. 최소 숫자가 너무 빡시긴해..

N = 5
M = 3 
array = [8, 3, 7, 9, 2]
array2 = [5, 7, 9]

for i in range(M):
    if array2[i] in array:
        print("yes")
    else:
        print("no")

# 이렇게 간단하게 풀었지만, 이진 탐색으로 이용할 수 있음. 기본 코드와 동일
# 계수 정렬 이용.

n = int(input())

array = [0] * 1000000

# 가게에 있는 전체 부품 번호를 입력 받아서 기록
for i in input().split:
    array[int(i)] = 1

m = int(input())

x = list(map(int, input().split()))

for i in x:
    if i in array:
        print('yes', end = ' ')
    else:
        print('no', end = ' ')