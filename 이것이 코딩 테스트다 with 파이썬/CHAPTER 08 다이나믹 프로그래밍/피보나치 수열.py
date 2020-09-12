# 중복되는 연산을 줄이자. 
# 다이나믹 프로그래밍 : 간단하게 메모리를 조금 더 사용하더라도, 연산 속도를 증가시키는 방법

# 기존 코드

def pibo(n):
    if n == 1 or n == 2:
        return 1
    else:
        return pibo(n-1) + pibo(n-2)

print(pibo(4))

# DP
dp = [0] * 100

def dppibo(n):
    dp[1] = 1
    dp[2] = 1
    if dp[n] != 0:
        return dp[n]

    dp[n] = dppibo[n-2] + dppibo[n-1]
    return dp[n]

print(dppibo(4))