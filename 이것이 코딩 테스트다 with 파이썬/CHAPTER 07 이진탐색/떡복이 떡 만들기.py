# 떡볶이 떡 만들기

n, m = 4, 6
array = [19, 15, 10, 17]
min = 0
max = max(array)


def average(n,m, array, min, max):
    sum = 0
    for i in range(n):
        mid = (max + min) //2
        if array[i] < mid : continue
        
        dif =array[i]- mid
        sum = sum + dif
        
    if sum == m:
        return mid
    elif sum > m:
        return average(n, m, array, mid + 1, max)
    else:
        return average(n, m, array, min, mid - 1)
    

result = average(n, m, array, min, max)
print(result)

