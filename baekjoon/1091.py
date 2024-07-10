def cardPosition(N:int,P:list[int])->list[set[int]]:
  result = [set() for _ in range(3)]
  for i in range(N):
    result[P[i]].add(i)
  return result

def solution(N:int,P:list[int],S:list[int])->int:
  now_card = [i for i in range(N)] # 현재 카드가 어떤 순서로 배열되어 있는지 기록
  wanted_result = cardPosition(N,P) # [idx번 사람이 가져야할 카드 set]

  visit = set()
  cnt = 0
  while True:
    for i in range(N):
      if not now_card[i] in wanted_result[i%3]:
        break
    else:
      return cnt
    cnt += 1
    join_value = ''.join(map(str,now_card))
    if join_value in visit:
      return -1
    visit.add(join_value)

    temp = [0]*N
    for i in range(N):
      temp[S[i]] = now_card[i]
    now_card = temp
  return -1
# 입력
N = int(input())
P = list(map(int,input().split()))
S = list(map(int,input().split()))
ans = solution(N,P,S)
print(ans)