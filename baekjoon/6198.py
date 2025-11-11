import sys
input = sys.stdin.readline

def solution(N:int,dataList:list[int])->int:
  value = 0
  stack = [(dataList[-1],N-1)]
  L = N-1
  for i in range(L)[::-1]:
    high = dataList[i]
    while stack and stack[-1][0]<high:
      stack.pop()
    if not stack: value += L-i
    else: value += stack[-1][1]-i-1
    stack.append((high,i))
  return value

N = int(input()) # N <= 8만
highData = [int(input()) for _ in range(N)]
ans = solution(N,highData)
print(ans)