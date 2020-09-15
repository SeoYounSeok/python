# 만들 수 없는 금액
# N 개의 동전을 가지고 있습니다.
# N 개의 동전을 이용하여 만들 수 없는 양의 정수 금액 중 최솟값을 구하는 프로그램을 작성하시오.

# N = 5,  3,2,1,1,9 원 동전이라고 했을 때, 양의 정수 금액 중 최솟값은 8원 입니다.

# N = 3, 3,5,7 일 때 양의 정수 금액 중 최솟 값은 1원입니다.


n = int(input())
data = list(map(int, input().split()))
data.sort()

target = 1
for x in data:
    # 만들 수 없는 금액을 찾았을 때 반복 종료
    # 굳이 모든 값을 찾아서 계산할 필요 없음.
    if target < x:
        break
    target += x

# 만들 수 없는 금액 출력
print(target)
