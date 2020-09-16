# 알파벳 대문자와 숫자(0 ~ 9) 로만 구성된 문자열이 입력으로 주어집니다.
# 알파벳을 오름차순으로 정렬하여 이어서 출력한 후에, 그 뒤에 모든 숫자 값을 이어서 출력합니다.


S = "K1KA5CB7"
# S = sorted(S, reverse= True)
S = sorted(S)
a = ""
b = 0
print(S)

for i in S:
    if i.isalpha():
        a += i
    else:
        b += int(i)

print(a + str(b))