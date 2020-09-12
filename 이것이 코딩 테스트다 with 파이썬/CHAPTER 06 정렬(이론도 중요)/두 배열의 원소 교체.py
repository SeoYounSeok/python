n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a = a.sort()
# b.sort(reverse = True)
b = sorted(b, reverse= True)

for i in range(m):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break

for i in range(n):
    print(a[i], end=' ')
