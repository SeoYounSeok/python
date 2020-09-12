# 전에는 재귀함수로, 이번에는 반복문으로!

def binary_searchbinary_search(array, target, start, end):

    while start <= end:
        mid = (start + end)/2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

result = binary_searchbinary_search(array, target, 0, n-1)

# 이런식.?