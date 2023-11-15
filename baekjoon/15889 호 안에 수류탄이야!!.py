def solution(N:int,position:list[int],power:list[int])->bool:
    value = 0
    for i in range(N-1):
        value = max(value,position[i]+power[i])
        if value < position[i+1]:
            return False
    return True

N = int(input())
position = list(map(int,input().split()))
if N == 1:
    print("권병장님, 중대장님이 찾으십니다")
    exit()
power = list(map(int,input().split()))
ans = solution(N,position,power)
if ans:
    print("권병장님, 중대장님이 찾으십니다")
else:
    print("엄마 나 전역 늦어질 것 같아")