## 서울의 기온 데이터 분석하기 
```
- 기상자료개방포털 => 기후통계분석 => 기온분석

- 책에 적혀 있는 1904 01 01 ~ 2019 01 17
```
![image](https://user-images.githubusercontent.com/43161245/84876786-95b48080-b0c2-11ea-8ca8-1d36cfabf269.png)

### CSV 파일 이란?
```  
- 정부에서 운영하는 공공 데이터 포털이 제공하는 일반적인 파일 형식
```

### CSV 파일에서 데이터 읽어오기 
```
- csv.reader()
  csv 파일에서 데이터를 읽어오는 함수
  
- csv.writer()
  csv 파일에 데이터를 저장하는 함수
```
### Header 
```
헤더를 통해 각 열의 데이터가 어떤 의미를 갖는지 알 수 있다.

next() 함수는 첫 번째 데이터 행을 읽어오면서, 데어터의 탐색 위치를
다음 행으로 이동시켜주는 명령어입니다.
```
출처 : https://data.kma.go.kr/stcs/grnd/grndTaList.do?pgmNo=70
