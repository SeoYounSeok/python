def solution(progresses, speeds):
    answer = []
    # answer 에 넣어줄 값
    count = 0
    # 일자 계산합시다.
    days = 1

    for i in range(len(progresses)):
        if i == 0 and progresses[i] + speeds[i] * days >= 100:
            answer.append(1)
        elif i > 0 and progresses[i] + speeds[i] * days >= 100:
            answer[-1] += 1
        while progresses[i]+speeds[i]*days < 100:
            days += 1
            if progresses[i]+speeds[i]*days >= 100:
                count = 1
                answer.append(count)

    return answer
