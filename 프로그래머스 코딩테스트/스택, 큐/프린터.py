def solution(priorities, location):
    answer = 0
    max_priority = max(priorities)
    while True:
        current_priority = priorities.pop(0)
        if max_priority == current_priority:
            
            answer += 1
            
            if location == 0:
                break
            
            else:
                location -= 1
            
            max_priority = max(priorities)
        
        else:
            
            priorities.append(current_priority)
            
            if location == 0:
                location = len(priorities) - 1
                print(location)
            else:
                location -= 1
    
    return answer
