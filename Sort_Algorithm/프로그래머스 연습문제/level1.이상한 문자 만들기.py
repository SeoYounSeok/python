# 다른 사람이 만든 코드 
# split을 사용 안했습니다. 
def solution(s):
    answer = ""
    counter = 0
    for i in range(len(s)):
        if s[i] == " ":
            counter = 0
            answer += " "
        elif counter % 2 == 0:
            answer +=s[i].upper()
            counter +=1
        elif counter % 2 == 1:
            answer += s[i].lower()   
            counter +=1
    return answer
