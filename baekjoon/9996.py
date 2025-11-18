def solution(N:int,pattern:str,nameList:list[str])->list[str]:
  P = len(pattern)
  ls = list()
  target = pattern.split('*')
  T1,T2 = len(target[0]),len(target[1])
  for name in nameList:
    N = len(name)
    front = name[:T1]
    back = name[N-T2:]
    if (N+1<P) or not (front == target[0] and back == target[1]):
      ls.append('NE')
    else:
      ls.append('DA')
  return ls

N = int(input())  # N<=100
pattern = input()
nameList = [input() for _ in range(N)]
ans = solution(N,pattern,nameList)
print(*ans,sep='\n')