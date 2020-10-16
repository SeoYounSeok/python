def solution(n):
    answer = 0
    _str = ""

    while True:

        _plus = n % 3
        _str += str(_plus)
        if n // 3 == 0 :
            break

        n = n // 3 

    _str = reversed(_str)
    for idx, val in enumerate(_str):
        answer += 3 ** idx * int(val)


    return answer
