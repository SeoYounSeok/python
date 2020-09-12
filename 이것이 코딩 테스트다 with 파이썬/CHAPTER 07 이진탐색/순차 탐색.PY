# 범위를 반씩 좁혀가는 탐색
# 순차 탐색 : 리스트 안에 있는 특정한 데이터를 찾기 위해서 앞에서부터 데이터를 하나씩 확인하는 과정

def sequential_search(n, target, array):
    for i range(n):
        if array[i] == targer:
            return i + 1

print("문자열 입력하세요")

input_data = input().split()
n = int(input_data[0])
target = input_data[1]

print("원소 개수만큼 문자열 작성하세요")
array = input().split()

print(sequential_search(n,target,array))