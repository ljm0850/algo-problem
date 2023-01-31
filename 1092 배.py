import sys
input = sys.stdin.readline
def solution(cranes:list[int],boxes:list[int],N:int,M:int):
    newBox = [0]*N
    target = [i for i in range(N)]
    c = 0
    while boxes:
        box = boxes.pop()
        if box <= cranes[c]:
            newBox[c] += 1
        else:
            while box > cranes[c]:
                c += 1
                if c >= len(cranes):
                    return -1
            newBox[c] += 1
    ans = 0
    while M:
        idx = 0
        ans += 1
        while idx < N:
            T = target[idx]
            if T == -1:
                idx += 1
            elif newBox[T]:
                newBox[T] -= 1
                M -= 1
                idx += 1
            else:
                target[idx] -= 1
    return ans

N = int(input())
cranes = list(map(int,input().split()))
cranes.sort()
M = int(input())
boxes = list(map(int,input().split()))
boxes.sort(reverse=True)
answer = solution(cranes,boxes,N,M)
print(answer)