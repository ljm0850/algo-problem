import sys
input = sys.stdin.readline
def findDiv(N,num):
    cnt = 0
    div = num
    while div<=N:
        cnt += N//div
        div *= num
    return cnt

T = int(input())
for tc in range(T):
    N = int(input())
    ans = findDiv(N,5)
    print(ans)