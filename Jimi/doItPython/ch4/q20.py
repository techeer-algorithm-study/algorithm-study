import sys
input = sys.stdin.readline
print = sys.stdout.write

def merge_sort(left, right):
    if left < right:
        mid = int((left + right) / 2) # 중간 위치 계산하여 분할
        merge_sort(left, mid) # 앞쪽 부분 정렬
        merge_sort(mid+1, right) # 뒤쪽 부분 정렬 
        for i in range(left, right+1): # 임시 리스트에 저장 
            list[i] = sorted[i]
        merge(left, mid, right) # 정렬된 2개 배열 합병
    else: return


def merge(left, mid, right): 
    i = left # 정렬된 왼쪽 리스트에 대한 인덱스 
    j = mid + 1 # 정렬된 오른쪽 리스트에 대한 인덱스
    k = left # 정렬될 리스트에 대한 인덱스

    while i <= mid and j <= right: # 분할 정렬된 두 리스트 합병
        if list[i] <= list[j]:
            sorted[k] = list[i]
            k += 1
            i += 1
        else:
            sorted[k] = list[j]
            k += 1
            j += 1
    
    while i <= mid: # 남아 있는 값들 일괄 복사 
        sorted[k] = list[i]
        k += 1
        i += 1
    
    while j <= right:
        sorted[k] = list[j]
        k += 1
        j += 1


n = int(input()) # 정렬할 수 개수 입력받기
sorted = [0] * int(n+1) # 정렬할 리스트 
list = [0] * int(n+1) # 정렬할 임시 리스트


for i in range(1, n+1): # 배열 입력받기 
    sorted[i] = int(input()) 

merge_sort(1, n) # 병합 정렬 수행 (1은 배열의 시작, n은 배열의 끝)

for i in range(1, n+1):
    print(str(sorted[i]) + '\n')


