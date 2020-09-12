# data 1 번 정렬 후, 0번 출력 

n = int(input())

array = []
for  i range(n):
    input_data = input().split()

    array.append(input_data[0], input_data[1])

array = sorted(array, key= student: student[1])
# 파이썬에서 'lambda' 런타임에 생성해서 사용할 수 있는 익명 하뭇
# 일시적인 함수, 즉시 사용하고 버릴 수 있습니다. 
# lambda 는 리턴식이 고, 반환 값만 있습니다. 

# g = lambda x: x**2
# g2 = lambda x,y : x+y
for student in array

    print(student[0], end= ' ')

