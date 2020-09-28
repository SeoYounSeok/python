# 체육복 75/100 머가 틀린것인가?...

def solution(n, lost, reserve):
    
    if len(reserve) == 0:
        return n - len(lost)
    
    n = n - len(lost)
    count = 0
    for i in range(len(reserve)):
        if count == len(lost):
            return n
        
        num1 = reserve[i] + 1
        num2 = reserve[i] - 1
        
        if num1 in lost or num2 in lost:
            n += 1
            count += 1
    
    return n
