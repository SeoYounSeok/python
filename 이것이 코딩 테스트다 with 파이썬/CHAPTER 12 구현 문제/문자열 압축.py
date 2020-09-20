# 문자열 압축

s = "aabbaccc" # 7
s2 = "abcabcdede" # 8
max = len(s)//2
result = 0
# 입출력 예시 하나씩 짤랐을 때, 7
# 입출력 예시3 문자열을 3개 단위로 잘라 압축했을 때가 제일 작다.

# 많이 잘라도 최대 절반

def solution(s):
    # 3보다 작으면, len을 출력
    if len(s) < 3
        return len(s)
    
    answer = len(s)
    max_card = len(s)//2

    for interval in range(1, max_card + 1) :
        start = interval
        # prev 비교
        res = []
        pre_s = s[0:interval]
        num = 1
        while True:

            now_s = s[start: start+interval]

            if now_s == pre_s:
                num += 1
            else:
                res.append([num, pre_s])
                num = 1
                pre_s = now_s

            if start > len(s):
                break

            start += interval

        len_cand = 0

        for k in range(len(res)):
            if res[k][0] == 1:
                len_cand += len(res[k][1])
            
            else:
                len_cand += len(str(res[k][0]))
                len_cand += len(res[k][1])
            
            answer = min(answer,len_cand)

        return answer