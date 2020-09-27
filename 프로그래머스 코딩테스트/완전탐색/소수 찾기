# 소수 찾기 => 실패 후 코드 분석하겠습니다. 

from itertools import permutations

# 위에 import 로 가져와주세요.

def solution(numbers):
    count = 0
    test_number = []
    for i in range(len(numbers)):
        case = list(map(''.join,permutations(numbers,i+1)))
        
        print("case =" + str(case))
        
        for j, number in enumerate(case):
            test_number.append(int(number))
            print("test_number = " + str(test_number))
            
    # set 함수는 중복 제거용!
    test_number = list(set(test_number))
    print("set = " + str(test_number) )    
    for i, number in enumerate(test_number):
        if isPrime(number)== True:
            count +=1
         
    return count

# 소수 찾기 기본 

def isPrime(x):
    if x<2:
        return False
    else:
        for i in range(2,x):
            if x % i == 0:
                return False





- console 결과물
case =['0', '1', '1']
test_number = [0]
test_number = [0, 1]
test_number = [0, 1, 1]
set = [0, 1]
case =['01', '01', '10', '11', '10', '11']
test_number = [0, 1, 1]
test_number = [0, 1, 1, 1]
test_number = [0, 1, 1, 1, 10]
test_number = [0, 1, 1, 1, 10, 11]
test_number = [0, 1, 1, 1, 10, 11, 10]
test_number = [0, 1, 1, 1, 10, 11, 10, 11]
set = [0, 1, 10, 11]
case =['011', '011', '101', '110', '101', '110']
test_number = [0, 1, 10, 11, 11]
test_number = [0, 1, 10, 11, 11, 11]
test_number = [0, 1, 10, 11, 11, 11, 101]
test_number = [0, 1, 10, 11, 11, 11, 101, 110]
test_number = [0, 1, 10, 11, 11, 11, 101, 110, 101]
test_number = [0, 1, 10, 11, 11, 11, 101, 110, 101, 110]
set = [0, 1, 101, 10, 11, 110]
