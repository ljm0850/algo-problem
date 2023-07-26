
# 병합정렬(N logN) 이용
import sys
input = sys.stdin.readline
def merge_sort(ls:list[int])->list[int]:
    n = len(ls)
    if n > 1:
        m = n//2
        left = merge_sort(ls[:m])
        right = merge_sort(ls[m:])
        return merge(left, right)
    else:
        return ls

def merge(left:list[int],right:list[int])->list[int]:
    global cnt
    L,R = len(left),len(right)
    left_idx,right_idx = 0,0
    new_ls = []
    # swap 로직
    while left_idx < L and right_idx < R:
        if left[left_idx] <= right[right_idx]:
            new_ls.append(left[left_idx])
            left_idx += 1
        else:
            new_ls.append(right[right_idx])
            # Left의 남은 숫자 모두 right[right_idx]보다 크기에 L-left_idx 만큼 추가
            cnt += L - left_idx
            right_idx += 1
    # 남은 부분 털어내기
    new_ls += left[left_idx:]
    new_ls += right[right_idx:]
    return new_ls

N = int(input())
arr = list(map(int,input().split()))
cnt = 0
merge_sort(arr)
print(cnt)