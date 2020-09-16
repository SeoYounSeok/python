# 곱하기 혹은 더하기
# 숫자 (0부터 9)로만 이루어진 문자열 S가 주어졌을 때, 왼쪽부터 오른쪽으로 하나씩 'X' 또는 '+' 로 만들 수 있는 것을 생각해라

# 02984 # 답 : 576

# 567 답 : 210
# 입력값이  인트형이면?

a = "02984"
result = 0

for i in range(len(a)):
    # 0일 때도 있지만 1 일 때도 생각해야지 바보야 ㅡㅡ ..
    # if a[i] == "0" or result == 0:
    if num <= 1 or result <= 1:
        result += int(a[i])

    else:
        result *= int(a[i])

print(result) 
