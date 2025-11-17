# 좀 비효율적인듯

def check(value:str)->int:
  before_state = value[0]
  cnt = 0
  for state in value:
    if state != before_state:
      cnt += 1
      before_state = state
  return cnt

# 인풋 처리
N = int(input())
first,last,cnt = list(),list(),list()
for _ in range(N):
  value = input()
  cnt.append(check(value))
  first.append(value[0])
  last.append(value[-1])

# 로직
def recur(deepth:int,last_state:str,total:int)->None:
  global minValue
  if minValue <= total: return
  if deepth == 0:
    minValue = min(minValue,total)
    return
  for i in range(N):
    if visit[i]: continue
    visit[i] = True
    addedValue = 1 if last_state != first[i] else 0
    recur(deepth-1,last[i],total+cnt[i]+addedValue)
    visit[i] = False
  return

visit = [False]*(N)
minValue = 1001
for i in range(N):
  visit[i] = True
  recur(N-1,last[i],cnt[i])
  visit[i] = False
print(minValue)