# 볼링공 고르기 

# 이렇게 풀면 시간 초과 걸립니다  ^_^ 하하하...

# A,B 사람이 볼링을 치고 있습니다.
# 볼링공은 총 N 개 있으며, 각 볼링공마다 무게가 적혀있고 공의 번호는 1번 부터 순서대로 부여합니다.
# 볼링공은 1~M 까지 자연수

# N = 5 이고 M = 3 이며 각각의 무게가 차례대로 1,3,2,3,2

# (1,2),(1,3),(1,4),(1,5),(2,3),(2,5),(3,4),(4,5)
# 서로 무게가 다른 것을 고르려고 합니다.
# 결과적으로 두 사람이 공을 고르는 경우의 수는 8가지 
# 두 사람이 공을 고를 수 있는 경우의 수 


# 8 5
# 1 5 4 3 2 4 5 2  

# 답 : 25

# 경우의 수 고르는 문제

N = 8

result = 0

list = [1 ,5, 4, 3, 2, 4, 5, 2]

for i in range(N-1):
    for j in range(i + 1, N):
        if list[i] != list[j]:
            result += 1

print(result)
