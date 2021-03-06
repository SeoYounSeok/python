/* 
문제 1번 <사원> 테이블에서 '주소'만 검색하되 같은 '주소'는 한 번만 출력하세요.
*/

SELECT DISTINCT 주소 FROM 사원 

/* 
문제 2번 <사원> 테이블에서 '기본급'에 특별수당 10을 더한 월급을 'XX부서의 XXX의 월급 XXX' 형태로 출력하시오.
*/

SELECT 부서 + '부서의' AS 부서2, 이름 + '의 월급' AS 이름2, 기본급 + 10 AS 기본급 2
FROM 사원;

/* 
문제 3번 <사원> 테이블에서 '주로'를 기준으로 내림차순 정렬시켜 상위 2개 튜플만 검색하시오.
*/

SELECT TOP 2 * FROM 사원 ORDER BY 주소 DESC;

/* 
문제 4번 <사원> 테이블에서 '부서'를 기준으로 오름차순 정렬하고, 같은 '부서'에 대해서는 '이름'을 기준으로 내림차순 정렬시켜서 검색하시오.
*/

SELECT * FROM 사원 ORDER BY 부서 ASC, 이름 DESC;
