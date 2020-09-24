# 완주하지 못한 선수

def solution(participant, completion):
    answer = ''

    new_participant = sorted(participant)
    new_completion = sorted(completion)

    if new_participant[-1] != new_completion[-1]:
        return new_participant[-1]

    for i in range(len(new_completion)):
        if new_participant[i] != new_completion[i]:
            return new_participant[i]

    return answer
