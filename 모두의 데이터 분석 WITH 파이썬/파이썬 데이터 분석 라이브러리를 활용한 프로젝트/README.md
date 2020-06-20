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
### PANDAS (판다스) 라이브러리
```
* Pandas는 쉽고 직관적인 관계형 또는 분류된 데이터로 작업 할 수 있도록 설계된 
  빠르고 유연하며 표현이 풍부한 데이터 구조를 제공하는 Python 패키지이다.

* 설치법
  pip install pandas 
```
### Tip1. Pandas는 다음의 종류의 데이터에 적합한 분석 패키지이다.
```
* SQL 테이블 또는 Excel 스프레드 시트에서와 같이 이질적으로 유형이 지정된 열이있는 데이블 형식 데이터

* 정렬되고 정렬되지 않은 시계열 데이터

* 행 및 열 레이블이 포함 된 임의의 행렬 데이터 

* 다른 형태의 관찰 / 통계 데이터 세트
```
### Tip2. Pandas 의 구조 
```
* 1차원 배열 : Series 
* 2차원 배열 : DataFrame

* 행을 구분해주는 : 인덱스(index)
* 열을 구분해주는 : 컬럼(column)

* 이해가 조금 더 필요할 것 같다. 아직 잘 모르겠다.
```
![image](https://user-images.githubusercontent.com/43161245/85190602-d3005480-b2f4-11ea-8ea0-eb9302479fe1.png)

```
* 아직은 굉장히 모르는 부분 투성이...
```
