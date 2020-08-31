# 측정 시간은 각각의 컴퓨터마다 다를 수 있다.
# 삽입 행렬

array = [7,5,9,0,3,1,6,2,4,8]
# 삽입 행렬은 실행 시간 측면에서 선택정렬에 비해 더 효율적입니다.

for i in range(1, len(array)):
    for j in range(i,0, -1):
        if array[j] < array[j-1]: 
            array[j], array[j-1] = array[j-1], array[j]
        else:
            break


print(array)