def check(arr:list[str])->list[int]:
  R,C = len(arr)+1,len(arr[0])+1
  process = [-1]*C
  for i in range(C):
    process[i] = i

  for r in range(R-1):
    for c in range(C-1):
      if arr[r][c] == '*':
        continue
      process[c],process[c+1] = process[c+1],process[c]
  return process

def solution(k:int,n:int,result:str,arr:list[str])->str:
  result = list(map(lambda x: ord(x)-65,result))
  value = ''
  for i in range(n):
    if arr[i][0] == '?':
      if i == 0: process1 = list(range(k))
      else:process1 = check(arr[:i])
      if i != n-1: process2 = check(arr[i+1:])
      else: process2 = list(range(k))
      break
  dictProcess2 = dict()
  for i in range(k):
    dictProcess2[process2[i]] = i

  for i in range(k-1):
    if process1[i] != result[dictProcess2[i]]:
      if value and value[-1] == '-':
        return 'x'*(k-1)
      process1[i],process1[i+1] = process1[i+1],process1[i]
      value += '-'
    else:
      value += '*'
  return value

k = int(input())
n = int(input())
result = input()
arr = [input() for _ in range(n)]
ans = solution(k,n,result,arr)
print(ans)