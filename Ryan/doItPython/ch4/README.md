# Ch 3 Topics and Explanations:

## 1) 버블 정렬
- 스왑 연산
- 속도가 느린편이다 O(n^2)
## 2) 선택 정렬
- 효율적이지 않다
- 최소 최대 데이터가 나열된 순으로 찾아가며 선택하는 방법
- Ex. 최소 값을 찾아서 1번에 배치, 나머지에서 최소값 또 찾아서 2번.... and so on
## 3) 삽입 정렬
- 정렬된 데이터에 추가로 삽입
- 느리지만 구현하기 쉽다
## 4) 퀵 정렬
- pivot을 선정해서 less than or greater than 으로 정렬
## 5) 병합 정렬
- 분활정복
- 데이터를 분활 하고 정렬후 다시 합치는 방식
- o(nlogn)
## 6) 기수 정렬
- 값을 비교하지 않는 정렬
- O(kn)
- 리스트를 미리 설정 해두고 받은 값 순서대로 내보내기
- Ex. 1 4 5 will fill lst[1], lst[4], and lst[5]
- Print in order within list from 0