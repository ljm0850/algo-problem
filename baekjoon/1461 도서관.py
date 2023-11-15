# 로직
# 양수값 // 음수값으로 분리
# 분리된 값중 가장 먼 지점이 0에서 가까운 곳부터 처리(책 정리가 끝난 후 0으로 안돌아 와도 되서 마지막은 편도 처리가 가능하기에)
# 가장 먼 지점부터 M개 단위로 끊어서 책을 처리 => 가까운 지점부터 M개 끊을 경우 더 멀어짐
# => [1,2,3]을 2개씩 끊으면 [1,2],[3] => 총 거리 : 2*2(왕복) + 3*1(편도) = 7 // [1],[2,3] => 1*2(왕복) + 3*1(편도) = 5

def div_books(arr:list[int]):
    # part1은 양수값들, part2는 음수값들로 분리
    part1,part2 = list(),list()
    for num in arr:
        if num > 0:
            part1.append(num)
        else:
            part2.append(-num)
    part1.sort()
    part2.sort()
    return part1,part2

def solution(arr1:list[int],arr2:list[int],M:int):
    # arr2는 존재하지 않을 수 있음
    # arr1의 가장 큰 값이 arr2에 비해 0에 가까움
    value = 0
    value += count_moving(arr1,M)
    if arr2:
        value += arr1[-1]   # arr1에서 편도로 계산된 것을 왕복 처리 위함
        value += count_moving(arr2,M)
    return value

def count_moving(arr:list[int],M:int):
    # cnt 초기값이 arr[-1]인 이유 : 가장 먼 지점은 편도로 계산
    idx,cnt = len(arr)-M-1,arr[-1]
    while idx >= 0:
        cnt += 2 * arr[idx]
        idx -= M
    return cnt

N,M = map(int,input().split())
books_position = list(map(int,input().split()))
P1,P2 = div_books(books_position)

if not P1:
    ans = solution(P2,P1,M)
elif not P2:
    ans = solution(P1,P2,M)
elif P1[-1] <= P2[-1]:
    ans = solution(P1,P2,M)
else:
    ans = solution(P2,P1,M)
print(ans)