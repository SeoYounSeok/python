# 이진 탐색
# 찾으려고하는 데이터와 중간점 위치에 있는 데이터를 반복적으로 비교해서 찾아내는 것.

# 이진 탐색에서는 sort로 되어있어야 하는 것 아닌가요?
# 재귀함수로 구현한 이진탐색

def binary_search(array, target, start, end):
    if start > end:
        return None
    
    mid = (start + end)/2
    
    if array[mid] == target:
        return mid
    
    # 만약에 중간 값돠 찾고자 하는 값이 작은 경우 왼쪽 확인
    if array[mid] > target:
        binary_search(n, target, start, mid-1)
    
    # 만약에 중간 값돠 찾고자 하는 값이 큰 경우 오른쪽 확인
    if array[mid] < target:
        binary_search(n, target, mid + 1, end)

result = binary_search(array, target, 0, n-1)
if result == None:
    print("없어!")
else:
    print(result + 1)