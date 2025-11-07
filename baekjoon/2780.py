import sys
input = sys.stdin.readline

def solution(testCase:list[int])->list[int]:
  mod = 1234567
  graph = [[7],[2,4],[1,3,5],[2,6],[1,5,7],[2,4,6,8],[3,5,9],[4,8,0],[5,7,9],[6,8]]
  maxN = max(testCase)
  record = [[0]*10 for _ in range(maxN+1)]
  for num in range(10):
    record[1][num] = 1
  
  for deepth in range(2,maxN+1):
    for num in range(10):
      for nextNum in graph[num]:
        record[deepth][num] += record[deepth-1][nextNum]
      record[deepth][num] %= mod
  returnValueList = list()
  for N in testCase:
    returnValueList.append(sum(record[N])%mod)
  return returnValueList

T = int(input())
testCase = [int(input()) for _ in range(T)]
ans = solution(testCase)
print(*ans,sep='\n')