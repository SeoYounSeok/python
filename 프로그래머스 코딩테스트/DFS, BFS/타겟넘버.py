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

  DFS(numbers, target, idx+1, value + numbers[idx])
  DFS(numbers, target, idx+1, value - numbers[idx])
  
  
def solution(numbers, target):
  global answer
  DFS(numbers, target, 0, 0)
  return answer  
