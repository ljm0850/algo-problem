import math
def createPrimeNumberArr(maxValue):
  numbers = [False]*2+[True]*(maxValue-1)
  for num in range(2,maxValue):
    if numbers[num] == False:
      continue
    for multiple in range(2*num,maxValue+1,num):
      numbers[multiple] = False
  primeNums = list()
  for i in range(2,maxValue+1):
    if numbers[i]:primeNums.append(i)
  return primeNums

def solution(S,E):
  maxRange = math.ceil(math.sqrt(B))
  primeNumArr = createPrimeNumberArr(maxRange)
  ans = 0
  for num in primeNumArr:
    value = num * num
    while value <= B:
      if value >= A: ans += 1
      value *= num
  return ans

A,B = map(int,input().split())
ans = solution(A,B)
print(ans)