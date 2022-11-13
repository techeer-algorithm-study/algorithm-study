#  수 N개를 오름차순 정렬 했을 때 앞에서 부터 K 번째에 있는 수를 구하여라.
N, K = map(int, input().split())        # N은 숫자 개수 , K는 앞에서 부터 K번 째 수 선언
A = list(map(int, input().split()))     # A 는 숫자 데이터 저장 리스트


def quick(S, E, K):         # 퀵 정렬 선언 --> S는 시작, E는 종료 , K 는 K번쨰 수
    global A                # 글로벌 전역변수 A 이용하겠다
    if S < E:               # 만약 시작S가 E보다 작으면
        pivot = partition(S, E) # 피벗 = partition (S,E) 이용
        if pivot == K:      # 구하고자 하는 K가 피벗이라면 리턴
            return
        elif K < pivot:     # 구하고자 하는 K가 피벗보다 작으면 --> 피벗 기준 왼쪽 그룹만 정혈
            quick(S, pivot - 1, K)
        else:               # 구하고자 하는 K가 피벗보다 크면 --> 피벗 기준 오른쪽 그룹만 정혈
            quick(pivot + 1, E, K)

def swap(i, j):             # swap 미리 선언
    global A
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

def partition (S, E):       # partition (S,E) 미리 선언
    global A

    if S + 1 == E:          # S 다음이 E 라면
        if A[S] > A[E]:     # S 다음 값이 E 값이라면
            swap(S , E)     # swap 함수 실행
        return E 

    M = (S + E) // 2        # 중앙값 M 구하기
    swap(S, M)              # 중앙값과 S값 스왑
    pivot = A[S]            # 피벗 값을 시작위치로 설정
    i = S + 1               # i 시작 값 설정
    j = E                   # j 끝 값 설정
    while i <= j:           # i < j 일 때
        while pivot < A[j] and j > 0:        # 피벗 값이 j보다 작으면 j를 왼쪽으로 이동
            j = j - 1 
        while pivot > A[i] and i < len(A)-1: # 피벗 값이 i보다 크면 i를 오른쪽으로 이동
            i = i + 1
        if i <= j:          # i 와 j 가 인접했을때 스왑 실행
            swap()
        

    A[S] = A[j]             # 피벗 값을 경계 인덱스에 저장한다 
    A[j] = pivot
    return j

quick(0, N - 1, K - 1)      # 퀵 정렬 실행
print(A[K - 1])             # 구하고자 하는 K 값 출력
