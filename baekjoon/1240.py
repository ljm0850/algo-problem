def findLength(s:int,e:int,N:int):
  global record
  if record[s][e]:
    return record[s][e]

  stack = [(s,0)]
  visit = [False]*(N+1)
  visit[s] = True
  while stack:
    node,totalLength = stack.pop()
    for nextNode,length in graph[node]:
      if visit[nextNode]: continue
      visit[nextNode] = True
      nextLength = totalLength + length
      record[s][nextNode] = nextLength
      if nextNode == e:
        return nextLength
      stack.append((nextNode,nextLength))
  return 0

N,M = map(int,input().split())
graph = [[] for _ in range(N+1)]
record = [[0]*(N+1) for _ in range(N+1)]
for _ in range(N-1):
  aNode,bNode,length = map(int,input().split())
  graph[aNode].append((bNode,length))
  graph[bNode].append((aNode,length))

for _ in range(M):
  aNode,bNode = map(int,input().split())
  value = findLength(aNode,bNode,N)
  print(value)