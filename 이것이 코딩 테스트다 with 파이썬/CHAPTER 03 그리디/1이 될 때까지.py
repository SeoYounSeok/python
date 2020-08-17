# 1이 될 때까지 

n, m = map(int, input().split())
result = 0

while n > 1 :
    if n % m == 0 :
        n /= m
        result += 1
    else :
        n -= 1
        result += 1
        print(result)


print(result)