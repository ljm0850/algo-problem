import sys
input = sys.stdin.readline
N = int(input())
arr = [int(input()) for _ in range(N)]
arr.sort()
answer = 0
for i in range(N):
  answer += abs((i+1)-arr[i])
print(answer)