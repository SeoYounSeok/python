# 효율적인 화폐 구성

n = 2
m = 15

array = [2, 3]

dp = [10001] * m + 1
# 16 칸 짜리 10001

dp[0] = 0

for i in range(n):
    # m 까지 라서,
    for j in range(array[i], m + 1):
        if dp[j - array[i]] != 10001: # i-k 원을 만드는 방법이 존재하는 경우
            dp[j] = min(dp[j], dp[j - array[i]] + 1)
if dp[m] == 10001:
    print(-1)
else :
    print(dp[m])
