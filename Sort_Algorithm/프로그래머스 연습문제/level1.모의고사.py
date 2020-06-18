def solution(answers):
    answer = []
    dap1 = [1,2,3,4,5]
    dap2 = [2,1,2,3,2,4,2,5]
    dap3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0,0,0]

    for i in range(len(answers)):
        if answers[i] == dap1[i % len(dap1)]:
            score[0] += 1
        if answers[i] == dap2[i % len(dap2)]:
            score[1] += 1
        if answers[i] == dap3[i % len(dap3)]:
            score[2] += 1
            
    max_score = max(score)
    
    for i in range(3):
        if score[i] == max_score:
            answer.append(i + 1)

    return answer
