# N 개 이고 항상 짝수의 개수가 들어온다.


# N = list(map(int,input().split()))

data = "123402"

sumLeft = 0
sumRight = 0

mid = len(data) // 2

print(mid)

for i in range(mid):
    sumLeft += int(data[i])

for i in range(mid,len(data)):
    sumRight += int(data[i])

print(sumLeft)
print(sumRight)

if sumRight == sumLeft:
    print("LUCKY")

else:
    print("READY")