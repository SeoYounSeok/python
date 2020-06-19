### 파이썬 데이터 분석 라이브러리를 활용한 프로젝트
```
* matplotlib 홈페이지는 데이터 시각화와 관련된 다양한 예시

* matplotlib.org 접속 후 tutorials 메뉴를 확인
```
![image](https://user-images.githubusercontent.com/43161245/85098153-b997d380-b234-11ea-8005-e3da0a3aeac0.png)

### numpy 라이브러리
```
* numpy 라이브러리를 사용한 코드와 파이썬 리스트를 사용한 코드의 실행 결과는 똑같지만,
  numpy 라이브러리를 사용한 경우가 훨씬 적은 수의 코드로 작성하여 간결합니다.
  
* numpy 라이브러리를 배우면 숫자 데이터를 더 쉽게 다룰 수 있다.
```
![image](https://user-images.githubusercontent.com/43161245/85122300-49ec0d80-b261-11ea-84f2-acdfbdaa692d.png)

### numpy 라이브러리 정리 - 1
```
* numpy array
  - 다양한 데이터 타입을 담을 수 있었던 리스트와 달리, 
    한 가지 타입의 데이터만 저장할 수 있다.
    
* zeros(10) # 0으로 이루어진 크기가 10인 배열 생성

* ones(10) # 1으로 이루어진 크기가 10인 배열 생성

* eye(3) # 아래 !

  [[1,0,0],
   [0,1,0],
   [0,0,1]]
```
### numpy 라이브러리 정리 - 2
```
* arange() = for 배열 생각

EX1)  
  print(np.arange(3)) # arange() 함수에 1개 값 입력
  print(np.arange(3,7)) # arange() 함수에 2개 값 입력
  print(np.arange(3,7,2)) # arange() 함수에 3개 값 입력
  
  [0 1 2]
  [3 4 5 6]
  [3 5]

EX2)  
  a = np.arange(1,2,0.1) # 1이상 2미만 구간에서 0.1 간격으로 실수 생성 
  b = np.linspace(1,2,11) # 1부터 2까지 11개 구간으로 나눈 실수 생성
  print(a)
  print(b)
  
  [1. 1.1. ~ 1.9]
  [1. 1.1 ~ 2.]
```
