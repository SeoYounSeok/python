# global 의 사용법

answer = 0

def DFS(numbers, target, idx, value):
  global answer
  N = len(numbers)
  if idx == N and value == target:
    answer += 1
    return 
  if idx == N:
    return 
  
  # 5개 개수 지정해두고, + 또는  - 를 통해서 나타내는 것!
  DFS(numbers, target, idx+1, value + numbers[idx])
  DFS(numbers, target, idx+1, value - numbers[idx])
  
  
def solution(numbers, target):
  global answer
  DFS(numbers, target, 0, 0)
  return answer  
