def checkQuest(skills:set):
  global quest
  cnt = 0
  for q in quest:
    for skill in q:
      if not skill in skills: break
    else: cnt += 1
  return cnt

def recur(n:int,totalSkill:set,lastSkill:int):
  if len(totalSkill) == n:
    return checkQuest(totalSkill)
  maxValue = 0
  for skill in range(lastSkill+1,2*n+1):
    totalSkill.add(skill)
    value = recur(n,totalSkill,skill)
    totalSkill.remove(skill)
    maxValue = max(maxValue,value)
  return maxValue

n,m,k = map(int,input().split())
quest = [set(map(int,input().split())) for _ in range(m)]
ans = recur(n,set(),0)
print(ans)